#!/bin/bash
set -e
VENV="/opt/netbox/venv"
MANAGE="/opt/netbox/netbox/manage.py"

git pull

source "$VENV/bin/activate"
pip install -e . --upgrade

python "$MANAGE" collectstatic --no-input
python "$MANAGE" migrate   # só necessário se houver modelos/migrations

systemctl restart netbox netbox-rq
echo "🟢 NetPing atualizado para $(python -c 'import importlib.metadata, sys; print(importlib.metadata.version("netbox-netping"))')"
