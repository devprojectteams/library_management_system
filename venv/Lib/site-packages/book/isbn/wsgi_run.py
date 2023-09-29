# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from book.isbn import wsgi

if __name__ == '__main__':
    server = make_server('localhost', 8080, wsgi.wsgi_app)
    server.serve_forever()
