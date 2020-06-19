import os
import datetime

from django.db import models
from django.db.models.signals import post_delete
from PIL import Image

from ynb_site.apps.minecraft.models import McServer
from .signals import delete_image


class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Categories"


class Picture(models.Model):
	minecraft_server = models.ForeignKey(McServer, on_delete=models.CASCADE, default=1)
	# category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200, default="pic")
	credits = models.CharField(max_length=200, help_text="Use commas if multiple.")
	image = models.ImageField(upload_to="gallery")

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return f"{self.minecraft_server.name} - {self.title}"

	def save(self):
		super().save()
		if self.image:
			image = Image.open(self.image.path)
			output_size = (800, 800)
			image.thumbnail(output_size)
			image.save(self.image.path)

post_delete.connect(delete_image, Picture)
