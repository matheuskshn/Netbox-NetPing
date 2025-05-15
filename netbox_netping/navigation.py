# netbox_netping/navigation.py
from django.urls import reverse
from netbox.plugins import PluginMenuItem, PluginMenuButton

button_ping_job = PluginMenuButton(
    link=lambda _: reverse(
        "extras:job_enqueue",                # rota que exibe o formulário
        kwargs={"job_class": "netbox_netping.jobs.PingJob"},
    ),
    title="Run Ping Job",
    icon_class="mdi mdi-play-circle-outline",
)

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_netping:home",
        link_text="Home",
        buttons=(button_ping_job,),
    ),
)
