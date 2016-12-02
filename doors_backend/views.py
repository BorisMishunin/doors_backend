# -*- coding: utf-8 -*-

import logging
import time
import requests
import doors_backend.localsettings as settings
from django.http import HttpResponseBadRequest, HttpResponse, QueryDict
import urlparse

# Get an instance of a logger
logger = logging.getLogger(__name__)
profile_logger = logging.getLogger('frontend_profile')

def format_function(func, *args, **kw):
    args = map(repr, args)
    args.extend(
        ['%s=%r' % (k, v) for k, v in kw.items()])
    return '%s(%s)' % (func.__name__, ', '.join(args))

def profile_decorator():
    def decorator(func):
        def replacement(*args, **kw):
            start_time = time.time()
            result = func(*args, **kw)
            end_time = time.time()
            profile_logger.info("Function call: {} Wall time: {:.2f} s".format(format_function(func, args, kw), end_time - start_time))
            return result
        return replacement
    return decorator

@profile_decorator()
def invoke_resources(sevice_name, request, url, params={}, method='get', data=None):
    if not params:
        params = request.GET.copy()

        # needs for lists in get
        for (k, v) in params.lists():
            if len(v) > 1:
                params[k] = v

    requests_args = {}

    headers = {'Content-Type': 'application/json'}


    requests_args['headers'] = headers
    requests_args['data'] = data or request.body
    requests_args['params'] = QueryDict('', mutable=True)
    requests_args['params'] = params

    response = requests.request(method, urlparse.urljoin(settings.services[sevice_name], '/resources/' + url), **requests_args)

    view_response = HttpResponse(
        response.content,
        status=response.status_code)

    excluded_headers = set([
        'connection', 'keep-alive', 'proxy-authenticate',
        'proxy-authorization', 'te', 'trailers', 'transfer-encoding',
        'upgrade',
        'content-encoding',
        'content-length',
    ])
    for key, value in response.headers.iteritems():
        if key.lower() in excluded_headers:
            continue
        view_response[key] = value

    return view_response

@profile_decorator()
def invoke_service(service_name, endpoint, params={}, method='get'):
    manager = getattr(requests, method)
    if method == 'get':
        resp = manager(settings.services[service_name] + '/' + endpoint,
                       params=params)
    else:
        resp = manager(settings.services[service_name] + '/' + endpoint,
                       data=params)
    if resp.ok:
        return resp.json()
    else:
        return {'code': resp.status_code, 'body': resp.text}

def getItems(request):
    """
    """
    if request.method == 'GET':
        response = invoke_resources('doors_goods_service', request, 'goods',
                              method='get')
        return response
    else:
        return HttpResponseBadRequest('Not valid request method')

def getGoodsType(request):
    """
    """
    if request.method == 'GET':
        response = invoke_resources('doors_goods_service', request, 'goods_type',
                              method='get')
        return response
    else:
        return HttpResponseBadRequest('Not valid request method')

def getActions(request):
    """
    """
    if request.method == 'GET':
        response = invoke_resources('doors_marketplace_service', request, 'actions',
                              method='get')
        return response
    else:
        return HttpResponseBadRequest('Not valid request method')

