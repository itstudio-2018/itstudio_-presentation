from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


from . import models
from show.models import Department
import json
import re
import random
import datetime

import logging
info_log = logging.getLogger('info')


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

    if models.Link.objects.filter(email=email):
        models.Link.objects.filter(email=email).delete()

    models.Link(email=email, code=code).save()

    msg = 'http://39.96.208.176/join/confirm/' + '?email=' + email + '&code=' + code
    send_mail('爱特工作室',
              msg,
              settings.EMAIL_FROM,
              [email],)


def confirm(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

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
        info_log.info("method_error")
        return HttpResponse(status=404)


@csrf_exempt
def apply(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'POST':
        content = {'status': ''}

        try:
            json_data = json.loads(request.body)
        except:
            json_data = {}
        if not json_data:
            info_log.info("json_error")
            content['status'] = 'json_error'
            return response_error(content)

        try:
            name = json_data['name']
        except:
            name = ''
        if not name:
            info_log.info("name_error")
            content['status'] = 'name_error'
            return response_error(content)

        if len(name) > 20:
            info_log.info("name_length_error")
            content['status'] = 'name_length_error'
            return response_error(content)

        try:
            phone_number = json_data['phone']
        except:
            phone_number = ''
        if not phone_number:
            info_log.info("empty_phone")
            content['status'] = 'phone_error'
            return response_error(content)

        if re.search(r'\D', phone_number):
            info_log.info("phone_type_error")
            content['status'] = 'phone_error'
            return response_error(content)

        if len(phone_number) != 11:
            info_log.info("phone_length_error")
            content['status'] = 'phone_error'
            return response_error(content)

        if models.Applicant.objects.filter(phone_number=phone_number):
            if models.Applicant.objects.filter(phone_number=phone_number)[0].status != 0:
                info_log.info("phone_error")
                content['status'] = 'phone_error'
                return response_error(content)

        try:
            email = json_data['email']
        except:
            email = ''
        if not email:
            info_log.info("empty_email")
            content['status'] = 'email_error'
            return response_error(content)

        if not re.search(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
            info_log.info("email_error")
            content['status'] = 'email_error'
            return response_error(content)

        if len(email) > 100:
            info_log.info("email_length_error")
            content['status'] = 'email_length_error'
            return response_error(content)

        if models.Applicant.objects.filter(email=email):
            if models.Applicant.objects.filter(email=email)[0].status != 0:
                info_log.info("already_error")
                content['status'] = 'already_error'
                return response_error(content)

        try:
            year = int(json_data['year'])
        except:
            year = 0
        if not year:
            info_log.info("year_error")
            content['status'] = 'year_error'
            return response_error(content)

        if year < 2000 or year > 9999:
            info_log.info("year_value_error")
            content['status'] = 'year_value_error'
            return response_error(content)

        try:
            college = json_data['college']
        except:
            college = ''
        if not college:
            info_log.info("college_error")
            content['status'] = 'college_error'
            return response_error(content)

        if len(college) > 20:
            info_log.info("college_length_error")
            content['status'] = 'college_length_error'
            return response_error(content)

        try:
            speciality = json_data['speciality']
        except:
            speciality = ''
        if not speciality:
            info_log.info("speciality_error")
            content['status'] = 'speciality_error'
            return response_error(content)

        if len(speciality) > 20:
            info_log.info("speciality_length_error")
            content['status'] = 'speciality_length_error'
            return response_error(content)

        try:
            department_id = json_data['department_id']
        except:
            department_id = 0
        if not department_id:
            info_log.info("empty_id")
            content['status'] = 'id_error'
            return response_error(content)

        the_department = Department.objects.filter(id=department_id)
        if not the_department:
            info_log.info("id_error")
            content['status'] = 'id_error'
            return response_error(content)
        the_department = the_department[0]

        try:
            code = json_data['code']
        except:
            code = ''
        if not code:
            info_log.info("empty_code")
            content['status'] = 'code_error'
            return response_error(content)

        if code != request.session.get('code', None):
            info_log.info("code_error")
            content['status'] = 'code_error'
            return response_error(content)

        models.Applicant(name=name,
                         phone_number=phone_number,
                         email=email,
                         year=year,
                         college=college,
                         speciality=speciality,
                         department=the_department
                         ).save()

        send(email)

        info_log.info("apply_success")
        content['status'] = 'ok'

        return response_success(content)
    else:
        info_log.info("method_error")
        return HttpResponse(status=404)


def get_status(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'GET':
        content = {'status': ''}

        try:
            email = request.GET.get('email')
        except:
            email = ''
        if not email:
            info_log.info("empty_error")
            content['status'] = 'email_error'
            return response_error(content)

        if not re.search(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
            info_log.info("email_error")
            content['status'] = 'email_error'
            return response_error(content)

        applicant = models.Applicant.objects.filter(email=email)
        if not applicant:
            info_log.info("wrong_email")
            content['status'] = 'msg_error'
            return response_error(content)

        info_log.info("get_status_success")
        content['status'] = 'ok'
        content['situation'] = applicant[0].status

        return response_success(content)
    else:
        info_log.info("method_error")
        return HttpResponse(status=404)


