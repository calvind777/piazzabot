from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if (request.GET):
        print(request.GET)
        print(request.GET['hub.challenge'])
        return HttpResponse(request.GET['hub.challenge'])
    else:
        return HttpResponse('hi')
