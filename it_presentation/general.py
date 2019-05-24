from django.shortcuts import render, redirect


def templates_redirect(requset, left_url):
    return redirect('/static/templates/'+left_url)


def js_redirect(requset, left_url):
    return redirect('/static/js/'+left_url)


def css_redirect(requset, left_url):
    return redirect('/static/css/'+left_url)


def dist_redirect(requset, left_url):
    return redirect('/static/dist/'+left_url)


def media_redirect(request, left_url):
    return redirect('/media/'+left_url)
