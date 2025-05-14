# netbox_netping/netbox_netping/jobs.py

from concurrent.futures import ThreadPoolExecutor
import re
from ipaddress import ip_address
from typing import Dict, List, Tuple, Optional

from pythonping import ping
from ipam.models import Prefix, IPAddress
from extras.models import CustomField
from netbox.jobs import Job
from netbox.plugins import get_plugin_config
from extras.scripts import MultiObjectVar, StringVar

class PingJob(Job):
    class Meta:
        name = "Ping prefixes / IPs"
        description = "Ping every IP in selected prefixes or manual list, update status and custom field."
        commit_default = False  # user must tick to write changes

    prefixes = MultiObjectVar(
        model=Prefix,
        required=False,
        label="Prefixes",
        help_text="Deixe em branco para todos os prefixos.",
    )

    ip_list = StringVar(
        required=False,
        label="IPs extras",
        help_text="192.0.2.1, 198.51.100.10 ... separados por espaço ou vírgula",
    )

def run(self, prefixes, ip_list, **kwargs):
        # ------------------------------------------------------------------ #
        # Configurações do plugin
        # ------------------------------------------------------------------ #
        cfg          = get_plugin_config("netbox_netping") or {}
        count        = cfg.get("PING_COUNT",   1)
        timeout      = cfg.get("PING_TIMEOUT", 1)
        workers      = cfg.get("PING_WORKERS", 32)
        status_up    = cfg.get("STATUS_UP",    "active")
        status_down  = cfg.get("STATUS_DOWN",  "deprecated")

        # ------------------------------------------------------------------ #
        # Campo personalizado (SELECT) usado para registrar o resultado
        # ------------------------------------------------------------------ #
        cf_ping: Optional[CustomField] = CustomField.objects.filter(name="ping_status").first()

        # ------------------------------------------------------------------ #
        # Construção da lista de endereços a pingar
        # ------------------------------------------------------------------ #
        addr_map: Dict[str, Optional[IPAddress]] = {}
        sel_prefixes = prefixes if prefixes else Prefix.objects.all()

        for pfx in sel_prefixes:
            for ip_obj in IPAddress.objects.filter(parent=pfx):
                addr_map[str(ip_obj.address.ip)] = ip_obj

        if ip_list:
            for token in re.split(r"[\s,]+", ip_list.strip()):
                if not token:
                    continue
                try:
                    addr_map.setdefault(str(ip_address(token)), None)
                except ValueError:
                    self.log_warning(f"‘{token}’ inválido, ignorado")

        if not addr_map:
            self.log_failure("Nenhum IP encontrado para pingar")
            return

        addrs = list(addr_map.keys())

        # ------------------------------------------------------------------ #
        # Função de ping (executada em paralelo)
        # ------------------------------------------------------------------ #
        def _probe(addr: str) -> Tuple[str, bool, float]:
            try:
                r = ping(addr, count=count, timeout=timeout, size=40)
                return addr, r.success(), r.rtt_avg_ms or 0.0
            except Exception:
                return addr, False, 0.0

        # ------------------------------------------------------------------ #
        # Execução em pool de threads
        # ------------------------------------------------------------------ #
        up = down = 0
        results: List[Tuple[str, bool, float]] = []
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for res in pool.map(_probe, addrs):
                results.append(res)

        # ------------------------------------------------------------------ #
        # Tratamento dos resultados
        # ------------------------------------------------------------------ #
        for addr, ok, latency in results:
            ip_obj = addr_map[addr]

            # Log de cada host
            if ok:
                up += 1
                self.log_success(f"{addr} UP – {latency:.2f} ms")
            else:
                down += 1
                self.log_warning(f"{addr} DOWN")

            # Persistência se o usuário marcou “commit”
            if self.commit and ip_obj:
                ip_obj.status = status_up if ok else status_down

                # Atualiza o campo personalizado (string do choice)
                if cf_ping:
                    ip_obj.custom_field_data["ping_status"] = (
                        "status_up" if ok else "status_down"
                    )
                ip_obj.save()

        self.log_info(
            f"Concluído: {up} UP, {down} DOWN, {len(addrs)} testados, workers={workers}"
        )


jobs = [PingJob]
