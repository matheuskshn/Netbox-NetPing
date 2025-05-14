# netbox_netping/netbox_netping/navigation.py
from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_netping:pingjob",
        link_text="Ping prefixes / IPs",
    ),
)
