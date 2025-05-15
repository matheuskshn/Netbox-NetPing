# netbox_netping/netbox_netping/views.py
"""Views do NetPing."""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "netbox_netping/home.html"
