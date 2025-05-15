# netbox_netping/__init__.py
"""NetPing – plugin mínimo para NetBox 4.3."""

from netbox.plugins import PluginConfig

# --------------------------------------------------------------------
# PluginConfig
# --------------------------------------------------------------------
class NetPingConfig(PluginConfig):
    name = "netbox_netping"          # import path (obrigatório)
    verbose_name = "NetPing"         # aparece no cabeçalho
    description = "Plugin mínimo que adiciona um item de menu."
    version = "0.1.0"
    base_url = "netping"             # /plugins/netping/
    min_version = "4.3"

    default_settings = {
        "PING_COUNT":   2,
        "PING_TIMEOUT": 1,
        "PING_WORKERS": 32,
        "STATUS_UP":    "active",
        "STATUS_DOWN":  "deprecated",
    }

    def ready(self):
        super().ready()
        # Importa os jobs para registrá-los
        from . import jobs  # noqa: F401  (importação intencional)
        
# NetBox exige a variável de módulo **config**

config = NetPingConfig
