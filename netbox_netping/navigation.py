# netbox_netping/netbox_netping/navigation.py
from netbox.plugins import PluginMenuItem

# Item simples dentro de “Plugins”
menu_items = (
    PluginMenuItem(
        link="home",             # rota do core → sempre resolvível
        link_text="NetPing demo",
    ),
)
