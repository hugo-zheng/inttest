import os, sys, base64, time


import protocol_pb2

def parse_message(message):
    mode = message.get('mode')
    try:
        event = protocol_pb2.Event()
        msg=message.get('body')
        Base64=base64.b64decode(msg)
        event.ParseFromString(Base64)
        print event
    except Exception, e:
        print ('error', e)

    return mode, event


def generate_message(e):
    #test echo
    _msg=e.SerializeToString()
    cnt=e.ByteSize()
    msg=base64.b64encode(_msg[:cnt])

    return msg
