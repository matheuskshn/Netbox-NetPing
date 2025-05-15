# netbox_netping/netbox_netping/config.py
"""Plugin configuration for NetPing."""
from netbox.plugins import PluginConfig


class NetPingConfig(PluginConfig):
    name = "netbox_netping"          # caminho Python do pacote
    verbose_name = "NetPing"         # nome visível na UI
    description = "Plugin mínimo que adiciona um item de menu simples."
    version = "0.1.0"
    base_url = "netping"             # /plugins/netping/
    min_version = "4.3"
    required_settings = []
    default_settings = {}
