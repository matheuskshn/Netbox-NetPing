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

# NetBox exige a variável de módulo **config**
config = NetPingConfig
