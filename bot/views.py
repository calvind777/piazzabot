from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
import json 

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
        receivedparams = json.loads(request.body)
        print(receivedparams)
        if ('entry' in receivedparams and 'messaging' in receivedparams['entry'][0]):
            print('entered')
            page_access_token = settings.PAGE_ACCESS_TOKEN
            senderID = receivedparams['entry'][0]['messaging'][0]['sender']['id']
            print(receivedparams['entry'][0])
            print(receivedparams['entry'][0]['messaging'][0])
            print(senderID)
            headers = {'Content-type': 'application/json'}
            msg = {'recipient':{'id':senderID}, 'message':{'text': 'Hi this is PiazzaBot. I don\'t do anything yet'}}
            r = requests.post('https://graph.facebook.com/v2.6/me/messages?access_token='+page_access_token,params=msg,headers=headers)
            print(r.text)

        response = HttpResponse('hi')
        response.status_code=200
        return response
