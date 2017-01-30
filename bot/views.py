from django.shortcuts import render
from django.http import HttpResponse

@method_decorator(csrf_exempt)
def index(request):
    if (request.GET):
        print(request.GET)
        print(request.GET['hub.challenge'])
        response = HttpResponse(request.GET['hub.challenge'])
        response.status_code=200
        return response
    else:
        print(request.POST)
        response = HttpResponse('hi')
        response.status_code=200
        return response
