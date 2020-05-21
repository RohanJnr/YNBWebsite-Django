from django.urls import path

from .views import Gallery, McServerGallery


urlpatterns = [
    path("gallery", Gallery.as_view(), name="gallery"),
    path("gallery/<str:minecraft_server>", McServerGallery.as_view(), name="mc_album"),
]