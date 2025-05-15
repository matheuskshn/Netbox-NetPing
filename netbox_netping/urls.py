# netbox_netping/netbox_netping/urls.py
"""Mapeia as URLs do plugin (prefixadas por /plugins/netping/)."""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
