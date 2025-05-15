# netbox_netping/__init__.py
"""
Pacote raiz carregado pelo NetBox.
Exibe a variável global `config`, apontando para a subclasse PluginConfig.
"""
# Import absoluto relativo (Python resolve a partir deste pacote)
from .netbox_netping.config import NetPingConfig as _NetPingConfig

# Variável que o NetBox procura:
config = _NetPingConfig
