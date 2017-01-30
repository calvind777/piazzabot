from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if (request.method=='GET'):
        print(request.GET)
        print(request.get_host())
        if ('hub.challenge' in request.content_params):
            response = HttpResponse(request.GET['hub.challenge'])
            response.status_code=200
            return response
        else:
            response = HttpResponse('try again')
            response.status_code=200
            return response
    else:
        print(request.POST)
        print(request.body)
        print(request.get_host())
        response = HttpResponse('hi')
        response.status_code=200
        return response
