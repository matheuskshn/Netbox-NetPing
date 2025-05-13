# NetPing – NetBox plugin to ping prefixes and IP addresses

Features
--------
* **Ping** every IP registered in one, many or all prefixes in NetBox
* **Ping** a single IP or a free list of IPs (space/comma‑separated)
* Saves the result back to *each IP object*:
  * `status`  → configurable mapping (default **Ativo/Obsoleto**)
  * Custom field **ping_status** (selection: `status_up` / `status_down`)
* Runs as a background **Job** (async, via `rqworker`)
* Parallel ICMP using a configurable worker pool

Installation (development mode)
-------------------------------
```bash
cd /opt/netbox/local
# copy or clone this folder
pip install -r netbox_netping/requirements.txt

# In NetBox configuration.py
PLUGINS = [
    "netbox_netping",
]

PLUGINS_CONFIG = {
    "netbox_netping": {
        "PING_COUNT": 1,          # packets per host
        "PING_TIMEOUT": 1,        # seconds per packet
        "PING_WORKERS": 32,       # parallel workers (set to CPU*4 or whatever)
        "STATUS_UP": "active",   # choices: active,reserved,deprecated,dhcp,slaac
        "STATUS_DOWN": "deprecated",
    }
}

sudo systemctl restart netbox netbox-rq
```

Usage
-----
1. **Tools → Jobs → Ping prefixes / IPs**
2. Escolha prefixos (ou deixe vazio para todos) e/ou informe IPs manuais.
3. Marque *Commit* se deseja que o Job grave os resultados (status & `ping_status`).
4. Acompanhe no log do Job.

Tips
----
* Para *todos* os endereços de um prefixo, inclusive não cadastrados, descomente a parte indicada em `jobs.py` – cuidado com faixas grandes (/16+).
* A latência média aparece no log; você pode mudar `PING_COUNT` para valores >1 se precisar de média mais confiável.
