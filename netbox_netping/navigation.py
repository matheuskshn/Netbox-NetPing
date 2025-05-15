# netbox_netping/navigation.py
from netbox.plugins import PluginMenuItem, PluginMenuButton

# Caminho absoluto até o formulário “Run Job”
PING_JOB_URL = "/extras/jobs/enqueue/netbox_netping.jobs.PingJob/"

# 1) Cria o botão (é um objeto, não uma tupla)
button_ping_job = PluginMenuButton(
    link=PING_JOB_URL,
    title="Run Ping Job",
    icon_class="mdi mdi-play-circle-outline",
)

# 2) Atribui o botão dentro de uma tupla ao menu
menu_items = (
    PluginMenuItem(
        link="plugins:netbox_netping:home",
        link_text="Home",
        permissions=[],          # visível a qualquer usuário autenticado
        buttons=(button_ping_job,),   # ← note a vírgula final
    ),
)
