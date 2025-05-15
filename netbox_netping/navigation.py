# netbox_netping/navigation.py
from netbox.plugins import PluginMenuItem, PluginMenuButton

button_ping_job = PluginMenuButton(
    link="plugins:netbox_netping:run_ping_job",
    title="Run Ping Now",
    icon_class="mdi mdi-play-circle-outline",
)

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_netping:home",
        link_text="Home",
        buttons=(button_ping_job,),
    ),
)
