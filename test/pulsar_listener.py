#!/usr/bin/python
"""WSGI server example"""
from __future__ import print_function


from pulsar.apps import wsgi
from pulsar.apps.wsgi import route


class Rout(wsgi.Router):

    @route('/game/', mothod='post')
    def game(self, request):
        print(request)
        return 'haha'

class Site(wsgi.LazyWsgi):

    def setup(self, environ):
        router = Rout('/')
        return wsgi.WsgiHandler([router])

if __name__ == '__main__':
    print('Serving on 8087...')
    wsgi.WSGIServer(Site()).start()
