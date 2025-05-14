# netbox_netping/netbox_netping/config.py

from netbox.plugins import PluginConfig

class NetPingConfig(PluginConfig):
    # --- Identificação ------------------------------------------------------
    name         = "netbox_netping"
    verbose_name = "NetPing – Prefix/IP Ping"
    description  = "Ping prefixes and IPs, updating status and custom field."
    version      = "0.3.2"

    # --- Créditos -----------------------------------------------------------
    author        = "Matheus Gomes"
    author_email  = "matheuskshn@gmail.com"

    # --- Roteamento ---------------------------------------------------------
    base_url = "netping"

    # --- Compatibilidade ----------------------------------------------------
    min_version = "4.0.0"
    max_version = "4.999"

    # --- Configurações padrão ----------------------------------------------
    default_settings = {
        "PING_COUNT":   1,
        "PING_TIMEOUT": 1,
        "PING_WORKERS": 32,
        "STATUS_UP":    "active",
        "STATUS_DOWN":  "deprecated",
        
    
    }
    queues = ["default"]

# NetBox busca uma variável - nível de módulo - chamada “config”
config = NetPingConfig
