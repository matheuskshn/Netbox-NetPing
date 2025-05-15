# netbox_netping/netbox_netping/navigation.py
"""Define o item de menu exibido em Plugins ▸ NetPing."""
from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_netping:home",
        link_text="Home",
        permissions=[],
    ),
)
