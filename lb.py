#!/usr/bin/env python
from time import gmtime, strftime
from bottle import route, run, template
import requests
from random import randint


nodes = [ 'http://localhost:91', 'http://localhost:92' ]


@route('/')
def index():
    random_node = randint(0,len(nodes)-1)
    print random_node
    r = requests.get(nodes[random_node])

    return strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) + " : we randomly called server {0}, and response was '{1}'".format(random_node + 1,r.text)

run(host='0.0.0.0', port=90)

