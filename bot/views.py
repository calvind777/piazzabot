from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if (request.GET):
        print(request.GET)
        print(request.GET['hub.challenge'])
        response = HttpResponse(request.GET['hub.challenge'])
        response.status_code=200
        return response
    else:
        response = httpResponse('hi')
        response.status_code=200
        return response
