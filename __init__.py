# netbox_netping/__init__.py
"""
Pacote raiz carregado pelo NetBox.  
Precisa expor `config = <PluginConfig>` para que o NetBox o aceite.
"""
from importlib import import_module

# Importa a classe NetPingConfig que está no sub-pacote real
NetPingConfig = import_module(
    "netbox_netping.netbox_netping.config"
).NetPingConfig

# Variável que o NetBox procura
config = NetPingConfig
