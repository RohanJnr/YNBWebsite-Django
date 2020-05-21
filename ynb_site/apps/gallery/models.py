import os

from django.db import models
from PIL import Image

from ynb_site.apps.minecraft.models import McServer


class Picture(models.Model):
    minecraft_server = models.ForeignKey(McServer, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="gallery")

    def save(self):
        super().save()
        if self.image:
            image = Image.open(self.image.path)
            output_size = (800, 800)
            image.thumbnail(output_size)
            image.save(self.image.path)
