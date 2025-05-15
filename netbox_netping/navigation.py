# netbox_netping/netbox_netping/navigation.py
from netbox.plugins import PluginMenuItem

# Item simples dentro do grupo “Plugins”
menu_items = (
    PluginMenuItem(
        link="home",           # rota core sempre presente
        link_text="NetPing demo",
    ),
)
