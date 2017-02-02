from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.template import loader
import requests
import json 

@csrf_exempt
def index(request):
    message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='

    if (request.method=='GET'):
        signintemplate = loader.get_template('bot/index.html')
        print(message_url)
        print(request.GET)
        print(request.get_host())
        if ('hub.challenge' in request.content_params):
            response = HttpResponse(request.GET['hub.challenge'])
            response.status_code=200
            return response
        else:
            response = HttpResponse('try again')
            response.status_code=200
            return HttpResponse(signintemplate.render(request))
    elif (request.method=='POST' and json.loads(request.body)['object']=='page'):
        
        print(request.body)
        receivedparams = json.loads(request.body)
        print(receivedparams)
        if ('entry' in receivedparams and 'messaging' in receivedparams['entry'][0]):
            print('entered')
            page_access_token = settings.PAGE_ACCESS_TOKEN
            senderID = receivedparams['entry'][0]['messaging'][0]['sender']['id']
            
            headers = {'Content-type': 'application/json'}
            msg = json.dumps({'recipient':{'id':senderID}, 'message':{'text': 'Hi this is PiazzaBot. I\'m your personal'
                ' Piazza assistant who\'ll automatically notify you when new instructor or pinned notes are posted.'
            }})
            signinmsg = json.dumps({'recipient':{'id':senderID}, 'buttons':[
                  {
                    "type":"web_url",
                    "url":"https://piazza-bot.herokuapp.com/bot/signin/",
                    "title":"Log in to Piazza",
                    "webview_height_ratio": "compact"
                  }
                ]

            })
            r = requests.post(message_url+page_access_token,data=msg,headers=headers)
            s = requests.post(message_url+page_access_token,data=signinmsg,headers=headers)
            print(s.text)

        response = HttpResponse('hi')
        response.status_code=200
        return response
    else:
        return HttpResponse

def signin(request):
    signintemplate = loader.get_template('bot/index.html')
    return HttpResponse(signintemplate.render(request))
