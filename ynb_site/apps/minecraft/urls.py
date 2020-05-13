from django.urls import path

from .views import DetailMcServer, ListMcServers


urlpatterns = [
    path("minecraft", ListMcServers.as_view(), name="all_mc_servers"),
    path("minecraft/<str:server_name>", DetailMcServer.as_view(), name="mc_server"),
]