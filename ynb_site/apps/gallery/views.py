from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from ynb_site.apps.home.models import Game

from .models import Picture
from ynb_site.apps.minecraft.models import McServer

class Gallery(View):
    """List mc_albums for all minecraft servers."""

    def get(self, request):
        """Handle get request."""
        mc_albums = []
        mc_servers = McServer.objects.all()

        for server in mc_servers:
            if server.picture_set.all():
                mc_albums.append(server.name)

        template_name = "gallery/list_mc_albums.html"
        context = {
            "mc_albums": mc_albums
        }
        if len(mc_albums) == 1:
            return redirect("mc_album", minecraft_server=mc_albums[0])

        return render(request, template_name, context)


class McServerGallery(View):
    """Show specific server album."""

    def get(self, request, minecraft_server):
        """Handle get request."""
        mc_server = get_object_or_404(McServer, name=minecraft_server)
        thumbnail = mc_server.thumbnail
        pictures = mc_server.picture_set.all()
        template_name = "gallery/mc_album.html"
        context  = {
            "pictures": pictures,
            "album": mc_server.name,
            "thumbnail": thumbnail
        }
        return render(request, template_name, context)
