#!/usr/bin/python
"""WSGI server example"""
from __future__ import print_function
from gevent.pywsgi import WSGIServer

from bottle import Bottle
app = Bottle()

STATUS_OK = '200 OK'
STATUS_NOT_FOUND = '404 Not Found'

CONTENT_TYPE = 'text/html'
#CONTENT_TYPE = 'application/x-protobuf'

@app.route('/')
def route():
    #print(request.__dict__)
    return 'Hello World!'

@app.route('/test')
def test():
    #print(request.__dict__)
    return 'Hello World!'


if __name__ == '__main__':
    print('Serving on 8087...')
    WSGIServer(('', 8087), app).serve_forever()
