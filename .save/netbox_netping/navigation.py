# netbox_netping/netbox_netping/navigation.py

from netbox.plugins import PluginMenu, PluginMenuItem

menu_items = PluginMenuItem(
    link="plugins:netbox_netping:ping",
    link_text="Executar ping",
)

menu = PluginMenu(
    label="NetPing",
    icon_class="mdi mdi-pulse",
    groups=(("Tools", (menu_items,)),),
)