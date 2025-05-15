# netbox_netping/netbox_netping/config.py
from netbox.plugins import PluginConfig           # novo caminho na v4ᵒ :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

class NetPingConfig(PluginConfig):
    #
    # 1) Nome COMPLETO do sub-pacote (obrigatório)  :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}
    #
    name = "netbox_netping.netbox_netping"

    #
    # 2) Metadados exibidos em System → Plugins
    #
    verbose_name = "NetPing (demo)"
    description  = "Demo – exibe apenas um item no menu."
    version      = "0.1.0"

    #
    # 3) Prefixo dos caminhos do plugin                      :contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}
    #
    base_url     = "netping"

    #
    # 4) Compatibilidade declarada
    #
    min_version  = "4.0.0"
    max_version  = "4.999"
