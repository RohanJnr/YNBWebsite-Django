from django.contrib import admin

from .models import McServer, ServerFeature, ServerRule, ServerEvent

admin.site.register(McServer)
admin.site.register(ServerFeature)
admin.site.register(ServerRule)
admin.site.register(ServerEvent)
