from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from . import models
import json
import re
import random
import datetime


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


def send(email):
    # msg code
    code = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    for i in range(20):
        code += base_str[random.randint(0, 61)]

    models.Link(email=email, code=code).save()

    msg = 'http://39.96.208.176/join/confirm/' + '?email=' + email + '&code=' + code
    send_mail('爱特工作室',
              msg,
              settings.EMAIL_FROM,
              [email],)


def confirm(request):
    if request.method == 'GET':
        try:
            email = request.GET.get('email')
        except:
            email = ''
        if not email:
            return HttpResponse(status=404)

        try:
            code = request.GET.get('code')
        except:
            code = ''
        if not code:
            return HttpResponse(status=404)

        link = models.Link.objects.filter(email=email, code=code)
        if not link:
            return HttpResponse(status=404)
        link = link[0]

        if link.expiration.replace(tzinfo=None) + datetime.timedelta(hours=8, minutes=10) < \
                datetime.datetime.now().replace(tzinfo=None):
            return HttpResponse(status=404)

        applicant = models.Applicant.objects.filter(email=email)
        if not applicant:
            return HttpResponse(status=404)
        applicant = applicant[0]

        applicant.status = 1
        applicant.save()

        link.delete()

        return HttpResponse(status=200)

    else:
        return HttpResponse(status=404)


@csrf_exempt
def apply(request):
    if request.method == 'POST':
        content = {'status': ''}

        try:
            json_data = json.loads(request.body)
        except:
            json_data = {}
        if not json_data:
            content['status'] = 'json_error'
            return response_error(content)

        try:
            name = json_data['name']
        except:
            name = ''
        if not name:
            content['status'] = 'name_error'
            return response_error(content)

        try:
            phone_number = json_data['phone']
        except:
            phone_number = ''
        if not phone_number:
            content['status'] = 'phone_error'
            return response_error(content)

        if re.search(r'\D', phone_number):
            content['status'] = 'phone_error'
            return response_error(content)

        if len(phone_number) != 11:
            content['status'] = 'phone_error'
            return response_error(content)

        try:
            email = json_data['email']
        except:
            email = ''
        if not email:
            content['status'] = 'email_error'
            return response_error(content)

        if not re.search(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
            content['status'] = 'email_error'
            return response_error(content)

        try:
            year = int(json_data['year'])
        except:
            year = 0
        if not year:
            content['status'] = 'year_error'
            return response_error(content)

        try:
            college = json_data['college']
        except:
            college = ''
        if not college:
            content['status'] = 'college_error'
            return response_error(content)

        try:
            speciality = json_data['speciality']
        except:
            speciality = ''
        if not speciality:
            content['status'] = 'speciality_error'
            return response_error(content)

        models.Applicant(name=name,
                         phone_number=phone_number,
                         email=email,
                         year=year,
                         college=college,
                         speciality=speciality).save()

        send(email)

        content['status'] = 'ok'

        return response_success(content)
    else:
        return HttpResponse(status=404)

