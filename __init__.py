# netbox_netping/__init__.py
"""
Pacote raiz carregado pelo NetBox: deve expor `config`.
"""
from .netbox_netping.config import NetPingConfig  # import relativo seguro

config = NetPingConfig
