# netbox_netping/netbox_netping/urls.py
"""Mapeia as URLs do plugin (prefixadas por /plugins/netping/)."""
from django.urls import path

from . import views

app_name = "netbox_netping"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
