# netbox_netping/netbox_netping/navigation.py

from netbox.plugins import PluginMenu, PluginMenuItem

menu = PluginMenu(
    label="NetPing",
    icon_class="mdi mdi-pulse",          # qualquer ícone da MDI
    groups=(
        (
            "Ferramentas",
            (
                PluginMenuItem(
                    link="plugins:netbox_netping:ping",  # veremos essa view a seguir
                    link_text="Executar ping",
                ),
            ),
        ),
    ),
)
