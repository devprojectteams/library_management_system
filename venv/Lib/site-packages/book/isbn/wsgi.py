# -*- coding:utf-8 -*-

import urlparse
from book import isbn
import functools

default_message = """\
book.isbn provide below urls:
 * /check10/<\d{10}>/
 * /check13/<\d{13}>/
 * /modulus11weight10to2/<\d9>/
 * /modulus11weight3/<\d12>/
 * /encode10to13/<\d{10}>/
 * /encode13to10/<\d{13}>/
"""


def check_args(num):
    def _decorator(func):
        @functools.wraps(func)
        def __decorator(*args, **kw):
            if  len(args) == num:
                return func(*args, **kw)
            else:
                raise Exception('argument is not %s' % str(num))
        return __decorator
    return _decorator


isbn.check10 = check_args(1)(isbn.check10)
isbn.check13 = check_args(1)(isbn.check13)
isbn.modulus11weight10to2 = check_args(1)(isbn.modulus11weight10to2)
isbn.modulus11weight3 = check_args(1)(isbn.modulus11weight3)
isbn.encode10to13 = check_args(1)(isbn.encode10to13)
isbn.encode13to10 = check_args(1)(isbn.encode13to10)


def wsgi_app(environ, start_response):
    split_result = urlparse.urlsplit(environ['PATH_INFO'])
    paths = filter(None, split_result[2].split('/'))
    headers = [('Content-Type', 'text/plain')]

    if not paths:
        start_response('200 OK', headers)
        return [default_message]

    api_name = paths[0]

    try:
        method = getattr(isbn, api_name)
    except Exception, e:
        status = '404 Not Found'
        start_response(status, headers)
        return [status]

    try:
        result = str(method(paths[1])).encode('utf-8')
    except Exception, e:
        status = '500 Internal Server Error'
        start_response(status, headers)
        return [status]

    start_response('200 OK', headers)
    return [result]


def app_factory(global_config, **local_conf):
    """ wsgi app factory for Paste """
    return wsgi_app
