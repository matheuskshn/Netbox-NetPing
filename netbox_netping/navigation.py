# netbox_netping/navigation.py
from netbox.plugins import PluginMenuItem, PluginMenuButton
from django.urls import reverse

menu_items = (
    PluginMenuItem(
        link=reverse("plugins:netbox_netping:job"),     # view gerada pelo Job
        link_text="Ping prefixes / IPs",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_netping:job",
                title="Run now",
                icon_class="mdi mdi-play",
            ),
        ),
    ),
)
