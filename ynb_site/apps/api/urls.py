from django.urls import path

from .views import YtPushNotification


urlpatterns = [
	path("api/yt-notification", YtPushNotification.as_view(), name="yt-notification")
]