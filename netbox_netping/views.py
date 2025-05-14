# netbox_netping/netbox_netping/views.py
from django.urls import reverse
from django.shortcuts import redirect
from netbox.views.generic.base import View
from .jobs import PingJob

class PingJobView(View):
    """
    Dispara o PingJob imediatamente e redireciona para o log do job.
    """
    def get(self, request, *args, **kwargs):
        job = PingJob.enqueue(commit=True)        # dispara no RQ
        return redirect(reverse("core:job", args=(job.id,)))
