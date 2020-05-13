from django.shortcuts import render, redirect
from django.views import View


class Home(View):
    """Home Page view."""

    def get(self, request):
        """Handle get request."""
        template_name = "home/index.html"
        context = {}
        return render(request, template_name, context)
