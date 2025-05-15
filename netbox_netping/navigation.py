# netbox_netping/navigation.py
from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_netping:home",
        link_text="Home",
        permissions=[],           # visível para qualquer usuário autenticado
    ),
)
