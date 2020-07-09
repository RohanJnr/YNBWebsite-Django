from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class YtPushNotification(APIView):
	"""Youtube push notification callback url."""

	def post(self, request, format=None):
		"""post request."""
		data = request.data
		print(data)
		return Response("Received", status=status.HTTP_200_OK)

	def get(self, request):
		"""Verify youtube subscription"""
		hub_challenge = request.query_params["hub.challenge"]
		print(hub_challenge)
		return Response(int(hub_challenge), status=status.HTTP_200_OK)
