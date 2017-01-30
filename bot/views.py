from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
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
        print(request.content_params)
        if ('entry' in request.body and 'messaging' in request.body.entry[0]):
            print('entered')
            page_access_token = PAGE_ACCESS_TOKEN
            senderID = request.body.entry[0].messaging[0].sender.id
            msg = {'recipient':{'id':senderID}, 'message':{'text': 'Hi this is PiazzaBot. I don\'t do anything yet'}}
            r = requests.post('https://graph.facebook.com/v2.6/me/messages?access_token='+page_access_token,params=msg)
            

        response = HttpResponse('hi')
        response.status_code=200
        return response
