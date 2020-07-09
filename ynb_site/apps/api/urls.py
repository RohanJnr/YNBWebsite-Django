from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import YtPushNotification


urlpatterns = [
	path("api/yt-notification", YtPushNotification.as_view(), name="yt-notification")
]

urlpatterns = format_suffix_patterns(urlpatterns)
