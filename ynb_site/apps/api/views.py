from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import defusedxml.ElementTree as XML


namespaces = {
	'yt': 'http://www.youtube.com/xml/schemas/2015',
	'xmlns': 'http://www.w3.org/2005/Atom'
}


class YtPushNotification(APIView):
	"""Youtube push notification callback url."""

	def post(self, request, format=None):
		"""post request."""
		response = request.body.decode('utf-8')
		root = XML.fromstring(response)

		for entry in root.findall('xmlns:entry', namespaces=namespaces):
			link = entry.find('xmlns:link', namespaces=namespaces).get('href')

		print(link)
			
		return Response("Received", status=status.HTTP_200_OK)

	def get(self, request):
		"""Verify youtube subscription"""
		hub_challenge = request.query_params["hub.challenge"]
		print(hub_challenge)
		return Response(int(hub_challenge), status=status.HTTP_200_OK)
