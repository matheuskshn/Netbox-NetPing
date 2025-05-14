# netbox_netping/navigation.py
from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_netping:job",   # view gerada automaticamente
        link_text="Ping prefixes / IPs",
        permissions=["netbox_netping.run_pingjob"],
    ),
)
