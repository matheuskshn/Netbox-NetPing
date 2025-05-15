# netbox_netping/views.py
"""Views do NetPing."""

from django.views.generic import TemplateView
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from .jobs import PingJob


class HomeView(TemplateView):
    template_name = "netbox_netping/home.html"


class TriggerPingJobView(View):
    """Enfileira o PingJob e redireciona o usuário."""
    def get(self, request, *args, **kwargs):
        PingJob.enqueue()                     # agenda job
        messages.success(request, "Ping job enfileirado!")
        return redirect(reverse("plugins:netbox_netping:home"))
