from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from . import models
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


def get_department(request):
    if request.method == 'GET':
        content = {'status': 'ok', 'num': 0, 'list': []}

        departments = models.Department.objects.filter(is_alive=True)

        num = len(departments)
        content['num'] = num

        for one in departments:
            content['list'].append({
                'name': one.name,
                'info': one.info,
            })

        return response_success(content)

    else:
        HttpResponse(status=404)


def get_story(request):
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
        return HttpResponse(status=404)


def get_member_list(request):
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
        return HttpResponse(status=404)


def get_member_of_the_year(request):
    if request.method == 'GET':
        content = {'status': 'ok', 'num': 0, 'list': []}
        try:
            year = int(request.GET.get('year'))
        except:
            year = 0
        if not year:
            content['status'] = 'year_error'
            return response_error(content)
        content['year'] = year

        members = models.Member.objects.filter(year=year)
        content['num'] = len(members)

        for one in members:
            content['list'].append({
                'name': one.name,
                'department': one.department.name,
                'image': one.image.url,
                'info': one.info,
            })

        content['status'] = 'ok'

        return response_success(content)

    else:
        return HttpResponse(status=404)


def get_work(request):
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
        return HttpResponse(status=404)


def get_comment_list(request):
    if request.method == 'GET':
        content = {'status': 'ok', 'list': [],
                   'total_num': 0, 'num_per_page': 10, 'num_in_page': 0,
                   'page': 0, 'total_page': 0}
        try:
            page = int(request.GET.get('page', default='1'))
        except:
            page = 0
        if not page:
            content['status'] = 'page_error'
            return response_error(content)

        all_comment_list = models.Comment.objects.all().order_by('-time')
        content['total_num'] = len(all_comment_list)

        paginator = Paginator(all_comment_list, 10)

        total_page = paginator.num_pages
        content['total_page'] = total_page
        if page > total_page:
            page = total_page
        if page < 1:
            page = 1

        page_of_list = paginator.page(page).object_list
        content['page'] = page

        content['num_in_page'] = len(page_of_list)

        for one in page_of_list:
            content['list'].append({
                'nickname': one.nickname,
                'head_image': one.head_image,
                'content': one.content,
                'time': str(one.time.strftime('%Y-%m-%d %H:%M:%S')),
                'reply': one.reply,
            })

        return response_success(content)
    else:
        return HttpResponse(status=404)
