# netbox_netping/netbox_netping/__init__.py
"""Top-level package for NetPing plugin."""
__version__ = "0.1.0"

from .config import NetPingConfig  # noqa

# NetBox espera uma variável de módulo chamada **config**
config = NetPingConfig
