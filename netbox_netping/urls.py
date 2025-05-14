# netbox_netping/netbox_netping/urls.py

from django.urls import path
from .views import PingJobView

app_name = "netping"

urlpatterns = (
    path("ping/", PingJobView.as_view(), name="ping"),
)
