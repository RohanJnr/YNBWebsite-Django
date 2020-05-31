from django.db import models
from django.db.models.signals import post_save

from .signals import limit_instances


class Game(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class LandingPage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "LandingPageText"
        verbose_name_plural = "LandingPageText"

class HomePageSection(models.Model):
    section_no = models.IntegerField(default=1)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


post_save.connect(limit_instances, LandingPage)