# netbox_netping/navigation.py
from netbox.plugins import PluginMenuItem, PluginMenuButton

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_netping:home",
        link_text="Home",
        permissions=[],           # visível para qualquer usuário autenticado
    ),
)

menu_buttons = (
    PluginMenuButton(
        link=lambda _: reverse(
            "extras:job_run",  # view core do NetBox
            kwargs={"job_class": "netbox_netping.jobs.PingJob"},
        ),
        title="Run Ping Job",
        icon_class="mdi mdi-play-circle-outline",
        color="green",
    ),
)