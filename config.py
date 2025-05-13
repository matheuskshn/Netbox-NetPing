# netbox_netping/config.py
from extras.plugins import PluginConfig


class NetPingConfig(PluginConfig):
    name = "netbox_netping"
    verbose_name = "NetPing – Prefix/IP Ping"
    description = "Ping prefixes and standalone IPs, updating their status fields."
    version = "0.2.0"
    base_url = "netping"

    default_settings = {
        "PING_COUNT": 1,
        "PING_TIMEOUT": 1,   # seconds
        "PING_WORKERS": 32,  # parallel threads
        "STATUS_UP": "active",       # maps to escolha “Ativo”
        "STATUS_DOWN": "deprecated", # maps to escolha “Obsoleto”
    }


config = NetPingConfig
