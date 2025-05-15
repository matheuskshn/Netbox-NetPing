# netbox_netping/netbox_netping/navigation.py
"""
Define itens de navegação segundo navigation.md.
Usaremos a lista `menu_items` para colocar o item dentro do
menu Plugins padrão.              :contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}
"""
from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="home",              # rota core garantida
        link_text="NetPing demo",
    ),
)
