"""
WSGI config for ynb_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ynb_site.settings')

application = get_wsgi_application()
