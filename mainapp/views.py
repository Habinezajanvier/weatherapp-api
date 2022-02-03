from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def getWeather(request, name):
    try:
        appId = "3c532881afa6630ff2a29d928a7246f2"
        URLS = "https://api.openweathermap.org/data/2.5/weather"
        PARAMS = {"q": name, "appId": appId, "units": "metric"}

        r = requests.get(url=URLS, params=PARAMS)
        data = r.json()
        responseJson = {
            "message": "Data fetched successfully",
            "data": data
        }
        return Response(responseJson, status=status.HTTP_200_OK)
    except:
        serverError = {"error": "Something went wrong, try again latter"}
        return Response(serverError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
