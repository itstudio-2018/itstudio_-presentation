from django.shortcuts import render, redirect

import logging
info_log = logging.getLogger('info')


def templates_redirect(request, left_url):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))
    return redirect('/static/templates/'+left_url)


def js_redirect(request, left_url):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))
    return redirect('/static/js/'+left_url)


def css_redirect(request, left_url):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))
    return redirect('/static/css/'+left_url)


def dist_redirect(request, left_url):
    info_log.info("ip %s url %s method %s" % (str(request.META.get('REMOTE_ADDR')), request.path, request.method))
    return redirect('/static/dist/'+left_url)

