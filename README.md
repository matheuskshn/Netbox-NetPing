# NetPing – NetBox plugin

# Features

* Ping every IP assigned to selected prefixes – or all prefixes – using NetBox ORM (no REST).
* Ping arbitrary list of IPs (comma/space‑separated).
* Parallel workers (configurable) via ThreadPool; ICMP using **pythonping**.
* Writes results back to each `IPAddress`:
  * `status` (configurable mapping: STATUS_UP / STATUS_DOWN)
  * custom field `ping_status` (choices values `status_up` / `status_down`)
* Exposed as a **Job** under *Tools → Jobs*.

# Installation

```bash
inside NetBox host
cd /opt/netbox/netbox/local
git clone https://github.com/your-org/netbox-netping.git
source /opt/netbox/venv/bin/activate
pip install -e netbox-netping
```

Add to `configuration.py`:

```python
PLUGINS = ["netbox_netping"]
PLUGINS_CONFIG = {
    "netbox_netping": {
        "PING_COUNT": 1,
        "PING_TIMEOUT": 1,
        "PING_WORKERS": 32,
        "STATUS_UP": "active",       map to NetBox choice slug
        "STATUS_DOWN": "deprecated",  map to NetBox choice slug
    }
}
```

Restart NetBox & worker. Run job from the UI.
