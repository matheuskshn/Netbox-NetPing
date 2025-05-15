# netbox_netping/netbox_netping/config.py
from netbox.plugins import PluginConfig
from .navigation import menu_items      # ← importamos explicitamente

class NetPingConfig(PluginConfig):
    name = "netbox_netping"
    verbose_name = "NetPing"
    description = "Plugin mínimo que adiciona um item de menu simples."
    version = "0.1.0"
    base_url = "netping"
    min_version = "4.3"

    # ← Atribuímos o menu aqui.
    menu_items = menu_items
