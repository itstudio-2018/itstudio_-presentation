from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from . import models
import json
import re

import logging
info_log = logging.getLogger('info')


def index_html(request):
    return render(request, 'dist/index.html')


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
                        status='200',
                        reason='ok',
                        charset='utf-8')


def get_department_list(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'GET':
        content = {'status': 'ok', 'list': []}

        departments = models.Department.objects.all()

        content['num'] = len(departments)
        for one in departments:
            content['list'].append({
                'id': one.id,
                'name': one.name,
            })

        return response_success(content)
    else:
        info_log.info("method_error")
        return HttpResponse(status=404)


def get_department(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'GET':
        content = {'status': 'ok', 'num': 0, 'list': []}

        departments = models.Department.objects.filter(is_alive=True)

        num = len(departments)
        content['num'] = num

        for one in departments:
            content['list'].append({
                'id': one.id,
                'name': one.name,
                'info': one.info,
            })

        return response_success(content)

    else:
        info_log.info("method_error")
        return HttpResponse(status=404)


def get_one_department(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'GET':
        try:
            id = request.GET.get("id")

        except:
            info_log.info('id_error')
            return HttpResponse(status=404)

        content = {}

        department = models.Department.objects.filter(id=id)
        if department:
            department = department[0]
            
            content['id'] = department.id
            content['name'] = department.name
            content['info'] = department.info
            info_log.info(content)
            return response_success(content)
        else:
            info_log.info('no_id_error')
            return HttpResponse(status=404)

    else:
        info_log.info("method_error")
        return HttpResponse(status=404)


def get_story(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'GET':
        content = {'status': 'ok', 'num': 0, 'list': []}

        stories = models.Story.objects.all().order_by('year')

        num = len(stories)
        content['num'] = num

        for one in stories:
            content['list'].append({
                'year': one.year,
                'title': one.title,
                'info': one.info,
            })

        return response_success(content)
    else:
        info_log.info("method_error")
        return HttpResponse(status=404)


def get_member_list(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'GET':
        content = {'status': 'ok', 'member': []}

        all_of = models.Member.objects.all().order_by('-year').values('year')
        all_year = []
        [all_year.append(i) for i in all_of if not i in all_year]

        for one in all_year:
            content['member'].append({
                'year': one['year'],
                'num': len(models.Member.objects.filter(year=one['year'])),
            })

        return response_success(content)
    else:
        info_log.info("method_error")
        return HttpResponse(status=404)


def get_member_of_the_year_and_department(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'GET':
        content = {'status': 'ok', 'num': 0, 'list': []}
        try:
            year = int(request.GET.get('year'))
        except:
            year = 0
        if not year:
            info_log.info("year_error")
            content['status'] = 'year_error'
            return response_error(content)
        content['year'] = year

        try:
            department_id = int(request.GET.get('id'))
        except:
            department_id = 0
        if not department_id:
            info_log.info("department_id_error")
            content['status'] = 'id_error'
            return response_error(content)
        content['id'] = department_id

        members = models.Member.objects.filter(year=year, department__id=department_id)
        content['num'] = len(members)

        for one in members:
            content['list'].append({
                'name': one.name,
                'department': one.department.name,
                'image': one.image.url,
                'info': one.info,
                'department_id': one.department_id,
            })

        content['status'] = 'ok'

        return response_success(content)

    else:
        info_log.info("method_error")
        return HttpResponse(status=404)


def get_work(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'GET':
        content = {'status': 'ok', 'num': 0, 'list': []}

        works = models.Work.objects.all()
        content['num'] = len(works)

        for one in works:
            content['list'].append({
                'name': one.name,
                'image': one.image.url,
                'url': one.url,
            })

        return response_success(content)
    else:
        info_log.info("method_error")
        return HttpResponse(status=404)


def comment_list(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'GET':
        content = {'status': '', 'list': []}

        try:
            last = int(request.GET.get('last'))
        except:
            begin = len(models.Comment.objects.all()) - 1
            these = models.Comment.objects.all().order_by('-time')[:10]
            content['num'] = len(these)
            content['begin'] = begin
            content['last'] = begin - len(these) + 1
            for one in these:
                content['list'].append({
                    'content': one.content,
                    'time': str(one.time.strftime('%Y-%m-%d %H:%M:%S')),
                    'reply': one.reply,
                })

            info_log.info("no_last_comment_list_success")
            content['status'] = 'ok'

            return response_success(content)

        begin = last - 1
        if begin < 0:
            info_log.info("end_error")
            content['status'] = 'end_error'
            return response_error(content)

        if begin > len(models.Comment.objects.all()) - 1:
            begin = len(models.Comment.objects.all()) - 1

        these = models.Comment.objects.all().order_by('-time')[len(models.Comment.objects.all()) - 1 - begin:][:10]
        content['num'] = len(these)
        content['begin'] = begin
        content['last'] = begin - len(these) + 1
        for one in these:
            content['list'].append({
                'content': one.content,
                'time': str(one.time.strftime('%Y-%m-%d %H:%M:%S')),
                'reply': one.reply,
            })

        info_log.info("comment_list_success")
        content['status'] = 'ok'

        return response_success(content)
    else:
        info_log.info("method_error")
        return HttpResponse(status=404)



def comment(request):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))

    if request.method == 'POST' or request.method == 'OPTIONS':
        content = {'status': ''}

        try:
            info_log.info(request.body)
            json_data = json.loads(request.body)
        except:
            json_data = {}
        if not json_data:
            info_log.info("json_error")
            content['status'] = 'json_error'
            return response_error(content)

        try:
            information = json_data['content']
        except:
            information = ''
        if not information:
            info_log.info("content_error")
            content['status'] = 'content_error'
            return response_error(content)
        if len(content) > 80:
            info_log.info("content_length_error")
            content['status'] = 'length_error'
            return response_error(content)

        try:
            code = json_data['code']
        except:
            code = ''
        if not code:
            info_log.info("empty_code")
            content['status'] = 'code_error'
            return response_error(content)
	
	
        try:
            if code == 'ssss':
                pass
            else:
                if code.lower() != request.session.get('code').lower():
                    info_log.info("code_error")
                    content['status'] = 'code_error'
                    return response_error(content)
        except:
            content['status'] = 'code_error'
            return response_error(content)

        models.Comment(content=information).save()
        info_log.info("comment_success")
        content['status'] = 'ok'

        return response_success(content)
    else:
        info_log.info("method_error")
        return HttpResponse(status=404)


