from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import json


def response_success(content):
    content = json.dumps(content)
    return HttpResponse(content,
                        content_type='application/json;charset = utf-8',
                        status='200',
                        reason='ok',
                        charset='utf-8')


def response_error(content):
    content = json.dumps(content)
    return HttpResponse(content,
                        content_type='application/json;charset = utf-8',
                        status='400',
                        reason='Bad Request',
                        charset='utf-8')


def send(request):
    if request.method == 'GET':
        content = {'status': ''}
        try:
            email = request.GET.get('email')
        except:
            email = ''
        if not email:
            content['status'] = 'email_error'
            return response_error(content)

        msg = 'Hello world'
        send_mail('爱特工作室',
                  msg,
                  settings.EMAIL_FROM,
                  [email],)

        content['status'] = 'ok'

        return response_success(content)
    else:
        return HttpResponse(status=404)




