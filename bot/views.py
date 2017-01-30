from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if (request.method=='GET'):
        print(request.GET)
        
        response = HttpResponse(request.GET['hub.challenge'])
        response.status_code=200
        return response
    else:
        print(request.POST)
        print(request.body)
        response = HttpResponse('hi')
        response.status_code=200
        return response
