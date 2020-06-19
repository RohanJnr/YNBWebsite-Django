from django.shortcuts import render, redirect
from django.views import View

from .models import LandingPage, HomePageSection

class Home(View):
    """Home Page view."""

    def get(self, request):
        """Handle get request."""
        section_1 = HomePageSection.objects.get(section_no=1)
        section_2 = HomePageSection.objects.get(section_no=2)
        landing_text = LandingPage.objects.first()
        context = {
            "landing_text": landing_text,
            "section_1": section_1,
            "section_2": section_2
        }
        template_name = "home/home.html"
        return render(request, template_name, context)
