#!/usr/bin/env python
from bottle import route, run, template
from random import randint
import sys

whoami = randint(1,2)
prt = 90 + whoami

@route('/hello/<name>')
def index(name):
    return template('Hello <b>{{name}}</b>!', name=name)

@route('/')
def index():
    return "I am server: {0}, and I'm running on port: {1}".format(whoami,prt)

run(host='0.0.0.0', port=prt)

