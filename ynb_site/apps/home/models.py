from django.core.exceptions import ValidationError
from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class LandingPage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if LandingPage.objects.count() > 0:
            raise ValidationError("There can only be 1 instance of this model.")
        return super().save()

    class Meta:
        verbose_name = "LandingPageText"
        verbose_name_plural = "LandingPageText"

class HomePageSection(models.Model):
    section_no = models.IntegerField(default=1)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
        