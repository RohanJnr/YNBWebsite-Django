from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import McServer


class ListMcServers(View):
    """Display information of all minecraft servers."""

    def get(self, request):
        """Handle get request."""
        if McServer.objects.count() == 1:
            server_name = McServer.objects.first().name
            return redirect("mc_server", server_name=server_name)

        mc_servers = McServer.objects.filter(display=True)
        template_name = "minecraft/list-servers.html"
        context = {
            "mc_servers": mc_servers
        }
        return render(request, template_name, context)


class DetailMcServer(View):
    """Detail view of a minecraft server."""

    def get(self, request, server_name):
        """Handle get request."""
        mc_server_object = get_object_or_404(McServer, name=server_name, display=True)
        template_name = "minecraft/detail-server.html"
        context = {
            "server": mc_server_object
        }
        return render(request, template_name, context)


class McStats(View):
    """Show minecraft stats of specific players."""

    def get(self, request):
        """Handle get request."""
        template_name = "minecraft/stats.html"
        context = {}
        return render(request, template_name, context)
