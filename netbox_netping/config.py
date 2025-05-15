# netbox_netping/netbox_netping/config.py
from netbox.plugins import PluginConfig


class NetPingConfig(PluginConfig):
    #
    # Import path COMPLETO deste sub-pacote
    #
    name = "netbox_netping.netbox_netping"

    # Metadados
    verbose_name = "NetPing (demo)"
    description  = "Demo – apenas um item de menu."
    version      = "0.1.0"

    # Prefixo na URL:  /plugins/netping/…
    base_url     = "netping"

    # Compatibilidade
    min_version  = "4.0.0"
    max_version  = "4.999"


# Opcional (não usado diretamente, mas mantém coesão)
config = NetPingConfig
