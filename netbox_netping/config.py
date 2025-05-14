# netbox_netping/config.py
from netbox.plugins import PluginConfig

class NetPingConfig(PluginConfig):
    name         = "netbox_netping"           # nome do pacote
    verbose_name = "NetPing (demo)"
    description  = "Demo: apenas um item de menu."
    version      = "0.0.1"
    base_url     = "netping"                  # cria /plugins/netping/ (não usado aqui)
    min_version  = "4.0.0"
    max_version  = "4.999"

config = NetPingConfig
