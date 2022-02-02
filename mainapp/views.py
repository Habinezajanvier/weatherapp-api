from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def getWeather(request, name):

    appId = "3c532881afa6630ff2a29d928a7246f2"
    URLS = "https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {"q": name, "appId": appId, "units": "metric"}

    r = requests.get(url=URLS, params=PARAMS)
    responseJson = r.json()
    return Response(responseJson)
