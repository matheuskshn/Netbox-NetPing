"""Top-level package for NetPing plugin."""
__version__ = "0.3.0"

from .config import NetPingConfig

# NetBox procura uma variável de módulo chamada `config`
config = NetPingConfig

# Opcional (legado); não atrapalha em NetBox 4.x
default_app_config = "netbox_netping.config.NetPingConfig"
