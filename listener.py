#!/usr/bin/python
#from __future__ import print_function

import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gevent.pywsgi import WSGIServer
from bottle import Bottle
from bottle import request
from pykka import ActorRegistry

from actors.base_actor import get_player

from settings import HOST_ADDRESS, HOST_PORT

STATUS_OK = '200 OK'
STATUS_NOT_FOUND = '404 Not Found'

# CONTENT_TYPE = 'text/html'
CONTENT_TYPE = 'application/x-protobuf'

app = Bottle()

@app.route('/test/')
def _test():
    return 'OK'

@app.route('/<pid>/game/', method='POST')
def _game(pid):
    message = request.forms
    message['mode'] = 'game'
    player = get_player(pid)
    resp = player.ask(message)
    return resp


@app.route('/<pid>/iap/', method='POST')
def _iap(pid):
    player = get_player(pid)
    print (ActorRegistry.get_by_urn(pid))
    future = player.proxy().pprint({'message':'%s' % pid})
    return future.get()

if __name__ == '__main__':
    print('Serving on %s:%s...' % (HOST_ADDRESS, HOST_PORT))
    WSGIServer((HOST_ADDRESS, HOST_PORT), app).serve_forever()

