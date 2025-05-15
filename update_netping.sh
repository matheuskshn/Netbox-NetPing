#!/usr/bin/env bash
# /opt/netbox_netping/update_netping.sh
#
# Atualiza o plugin netbox_netping no NetBox 4.3
# - Assume repositório git em /opt/netbox_netping
# - Assume virtualenv do NetBox em /opt/netbox/venv
# - Reinicia NetBox e o worker RQ ao final

set -euo pipefail

PLUGIN_DIR="/opt/netbox_netping"
VENV="/opt/netbox/venv"
MANAGE="/opt/netbox/netbox/manage.py"

echo "📥  Atualizando código-fonte em $PLUGIN_DIR ..."
cd "$PLUGIN_DIR"
git pull --ff-only

echo "🐍  Ativando virtualenv do NetBox ..."
source "$VENV/bin/activate"

echo "📦  Instalando/atualizando pacote (editable) ..."
pip install -e "$PLUGIN_DIR" --upgrade

echo "🎨  Coletando arquivos estáticos (caso existam) ..."
if ! python "$MANAGE" collectstatic --no-input; then
  echo "⚠️  'collectstatic' não disponível – pulando."
fi

echo "🗄️  Aplicando migrations (caso existam) ..."
python "$MANAGE" migrate --no-input

echo "🔄  Reiniciando serviços NetBox ..."
systemctl restart netbox netbox-rq

echo -n "🟢  NetPing atualizado para a versão "
python - <<'PY'
import importlib.metadata as md, sys
print(md.version("netbox_netping"))
PY
