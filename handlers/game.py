#!/usr/bin/python

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.protobuf import read_protobuf_string

def handle(req):
    name = req.forms.get('name')
    body = req.forms.get('body')
    print name
    print body
    return "name:%s, body:%s" % read_protobuf_string(name, body)

