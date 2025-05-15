# netbox_netping/jobs.py
#
# Background job que executa ping em IPs provenientes de Prefix/IPAddress
# ou digitados manualmente.

from __future__ import annotations
import re
from concurrent.futures import ThreadPoolExecutor
from ipaddress import ip_address
from typing import Dict, List, Tuple, Optional

from pythonping import ping

from ipam.models import Prefix, IPAddress
from extras.models import CustomField
from netbox.jobs import JobRunner
from netbox.plugins import get_plugin_config
from extras.scripts import MultiObjectVar, StringVar


class PingJob(JobRunner):
    """Ping múltiplos endereços em paralelo."""

    # ---------- Variáveis exibidas no formulário ----------
    prefixes = MultiObjectVar(
        model=Prefix,
        required=False,
        label="Prefixes",
        description="Deixe em branco para todos os prefixos.",
    )
    ip_list = StringVar(
        required=False,
        label="IPs extras",
        description="192.0.2.1, 198.51.100.10 ... separados por espaço ou vírgula",
    )

    class Meta:
        name = "Ping prefixes / IPs"

    # ---------- Lógica principal ----------
    def run(self, prefixes, ip_list, **kwargs):  # noqa: C901  (mantemos a função longa por simplicidade)
        # Configuração via PLUGINS_CONFIG ou valores-padrão
        cfg         = get_plugin_config("netbox_netping") or {}
        count       = cfg.get("PING_COUNT",   1)
        timeout     = cfg.get("PING_TIMEOUT", 1)
        workers     = cfg.get("PING_WORKERS", 32)
        status_up   = cfg.get("STATUS_UP",    "active")
        status_down = cfg.get("STATUS_DOWN",  "deprecated")

        # Campo customizado opcional (Select) para guardar “up/down”
        cf_ping: Optional[CustomField] = CustomField.objects.filter(name="ping_status").first()

        # --- constrói lista de IPs -------------------------------------------------
        addr_map: Dict[str, Optional[IPAddress]] = {}
        for pfx in (prefixes or Prefix.objects.all()):
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

        # --- função executada em paralelo -----------------------------------------
        def _probe(addr: str) -> Tuple[str, bool, float]:
            try:
                r = ping(addr, count=count, timeout=timeout, size=40)
                return addr, r.success(), r.rtt_avg_ms or 0.0
            except Exception:
                return addr, False, 0.0

        # --- execução --------------------------------------------------------------
        up = down = 0
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for addr, ok, latency in pool.map(_probe, addr_map.keys()):
                ip_obj = addr_map[addr]
                if ok:
                    up += 1
                    self.log_success(f"{addr} UP – {latency:.2f} ms")
                else:
                    down += 1
                    self.log_warning(f"{addr} DOWN")

                # grava o resultado se “commit” = True
                if self.commit and ip_obj:
                    ip_obj.status = status_up if ok else status_down
                    if cf_ping:
                        ip_obj.custom_field_data["ping_status"] = (
                            "status_up" if ok else "status_down"
                        )
                    ip_obj.save()

        self.log_info(f"Concluído: {up} UP, {down} DOWN, {len(addr_map)} testados, workers={workers}")


# NetBox precisa encontrar a variável “jobs”
jobs = [PingJob]
