#!/usr/bin/python
from __future__ import print_function

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gevent.pywsgi import WSGIServer
from bottle import Bottle
from pykka import ActorRegistry

from actors.base_actor import Greeter

STATUS_OK = '200 OK'
STATUS_NOT_FOUND = '404 Not Found'

CONTENT_TYPE = 'text/html' #CONTENT_TYPE = 'application/x-protobuf'

app = Bottle()

@app.route('/<pid>/game/', method='POST')
def _game(pid):
    greeter = Greeter.start(pid)
    greeter.ask({'message':'%s' % pid})
    return 'game'

@app.route('/<pid>/iap/', method='POST')
def iap(pid):
    g = Greeter.start()
    g.actor_urn = pid
    ActorRegistry.unregister(g)
    ActorRegistry.register(g)

    #greeter2 = Greeter.start(1).proxy()
    #greeter3 = Greeter.start(2).proxy()
    #greeter4 = Greeter.start(3).proxy()
    #greeter5 = Greeter.start(4).proxy()
    #a = ActorRegistry.get_all()
    #for i in a:
    #    ppid = i.proxy().pid.get()
    #    print (ppid, type(ppid))
    #    if ppid == '123':
    #        print('haha, got you')
    #    else:
    #        print(ppid)

    for i in ActorRegistry.get_all():
        print ('here')
        print(i.proxy().actor_urn.get(), type(i.proxy().actor_urn.get()))
        if i.proxy().actor_urn.get() == pid:
            print ('haha, got you')

    print ('=============')
    a = ActorRegistry.get_by_urn(pid)
    print (a)
    print ('=============')

    for i in ActorRegistry.get_all():
        print(i)
        print (i.__dict__)
        print ('here')
        print(i.proxy().actor_urn.get(), type(i.proxy().actor_urn.get()))
        if i.proxy().actor_urn.get() == 'asdf':
            print ('haha, got you')

    #future = greeter.pprint({'message':'%s' % pid})
    return 'as'
    #return future.get()


if __name__ == '__main__':
    print('Serving on 8088...')
    WSGIServer(('', 8088), app).serve_forever()

