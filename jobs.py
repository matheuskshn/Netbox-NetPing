# netbox_netping/jobs.py
import re
import concurrent.futures
from ipaddress import ip_address
from typing import Dict, Tuple, List, Optional

from pythonping import ping
from netaddr import IPNetwork

from extras.jobs import Job
from extras.models import CustomField, CustomFieldChoice
from ipam.models import Prefix, IPAddress
from utilities.forms import MultiObjectVar, StringVar
from utilities.utils import get_config


class PingJob(Job):
    class Meta:
        name = "Ping prefixes / IPs"
        description = "Ping every IP in selected prefixes or manual list and write back status."
        commit_default = False  # user decides if changes are saved

    prefixes = MultiObjectVar(
        model=Prefix,
        required=False,
        label="Prefixes",
        help_text="Selecione um ou mais prefixos (vazio = todos)",
    )

    ip_list = StringVar(
        required=False,
        label="IPs extras",
        help_text="IPs separados por vírgula ou espaço – ex.: 192.0.2.1 198.51.100.2",
    )

    def run(self, prefixes, ip_list, **kwargs):  # noqa: C901  (complexity ok for this context)
        cfg = get_config("netbox_netping")
        count = cfg.get("PING_COUNT", 1)
        timeout = cfg.get("PING_TIMEOUT", 1)
        workers = cfg.get("PING_WORKERS", 32)
        status_up = cfg.get("STATUS_UP", "active")
        status_down = cfg.get("STATUS_DOWN", "deprecated")

        # Fetch custom‑field choices
        cf_ping: CustomField = CustomField.objects.filter(name="ping_status").first()
        if not cf_ping:
            self.log_warning("Custom field 'ping_status' não encontrado – ignorando campo customizado")
            cf_choice_up = cf_choice_down = None
        else:
            cf_choice_up = (
                CustomFieldChoice.objects.filter(custom_field=cf_ping, value="status_up").first()
            )
            cf_choice_down = (
                CustomFieldChoice.objects.filter(custom_field=cf_ping, value="status_down").first()
            )

        # 1) Build address ↔ ip_obj mapping
        addr_map: Dict[str, Optional[IPAddress]] = {}

        sel_prefixes = prefixes if prefixes else Prefix.objects.all()

        for pfx in sel_prefixes:
            for ip_obj in IPAddress.objects.filter(parent=pfx):
                addr_map[str(ip_obj.address.ip)] = ip_obj

            # Uncomment to include ALL hosts, even não cadastrados – heavy on /16+ !
            # for host in IPNetwork(str(pfx)).iter_hosts():
            #     addr_map.setdefault(str(host), None)

        # manual list
        if ip_list:
            for token in re.split(r"[\s,]+", ip_list.strip()):
                if not token:
                    continue
                try:
                    addr_map.setdefault(str(ip_address(token)), None)
                except ValueError:
                    self.log_warning(f"'{token}' não é um IP válido – ignorado")

        if not addr_map:
            self.log_failure("Nenhum IP para testar")
            return

        addresses = list(addr_map.keys())

        def _worker(addr: str) -> Tuple[str, bool, float]:
            try:
                resp = ping(addr, count=count, timeout=timeout, size=40)
                return addr, resp.success(), resp.rtt_avg_ms or 0.0
            except Exception:
                return addr, False, 0.0

        # 2) Parallel ping
        up, down = 0, 0
        results: List[Tuple[str, bool, float]] = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            for res in executor.map(_worker, addresses):
                results.append(res)

        # 3) Process results & write‑back
        for addr, success, latency in results:
            ip_obj = addr_map[addr]
            if success:
                up += 1
                self.log_success(f"{addr} ONLINE – {latency:.2f} ms")
            else:
                down += 1
                self.log_warning(f"{addr} OFFLINE")

            if not self.commit:  # skip DB write if user unchecked commit
                continue
            # Update NetBox objects only when they exist
            if ip_obj:
                ip_obj.status = status_up if success else status_down
                if cf_ping and cf_choice_up and cf_choice_down:
                    ip_obj.custom_field_data["ping_status"] = (
                        cf_choice_up.pk if success else cf_choice_down.pk
                    )
                ip_obj.save()

        self.log_info(
            f"Ping concluído: {up} online, {down} offline, {len(addresses)} testados; "
            f"workers={workers}, timeout={timeout}s, count={count}pkt"
        )


jobs = [PingJob]
