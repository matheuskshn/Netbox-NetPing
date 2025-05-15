# netbox_netping/netbox_netping/config.py
from netbox.plugins import PluginConfig


class NetPingConfig(PluginConfig):
    # Nome COMPLETO do sub-pacote onde vivem config, navigation, etc.
    # Isso faz o NetBox importar netbox_netping.netbox_netping.navigation
    name = "netbox_netping.netbox_netping"

    # Metadados mostrados em System → Plugins
    verbose_name = "NetPing (demo)"
    description  = "Demo – apenas um item de menu."
    version      = "0.1.0"

    # Prefixo da URL: /plugins/netping/…
    base_url     = "netping"

    # Compatibilidade declarada
    min_version  = "4.0.0"
    max_version  = "4.999"


# Variável exigida pelo NetBox
config = NetPingConfig
