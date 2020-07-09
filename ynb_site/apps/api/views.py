from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class YtPushNotification(APIView):
	"""Youtube push notification callback url."""

	def post(self, request):
		"""post request."""
		data = request.data
		print(data)
		return Response("Received", status=status.HTTP_202_ACCEPTED)
