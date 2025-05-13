# ---------------------------
# netbox_netping/config.py
# ---------------------------
from netbox.plugins import PluginConfig


class NetPingConfig(PluginConfig):
    name = "netbox_netping"
    verbose_name = "NetPing – Prefix/IP Ping"
    description = "Ping prefixes and IPs, updating status and custom field."
    version = "0.3.0"
    base_url = "netping"
    min_version = "4.0.0"
    max_version = "4.999"

    default_settings = {
        "PING_COUNT": 1,
        "PING_TIMEOUT": 1,
        "PING_WORKERS": 32,
        "STATUS_UP": "active",
        "STATUS_DOWN": "deprecated",
    }


config = NetPingConfig
