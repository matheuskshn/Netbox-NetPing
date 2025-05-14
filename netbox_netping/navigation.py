# netbox_netping/navigation.py
from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_netping:job",     # view gerada pelo Job
        link_text="Ping prefixes / IPs",
        buttons=(),
    ),
),
