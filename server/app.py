#!/usr/bin/env python3

from app import app
from flask import Flask, request

request_context = app.test_request_context()
request_context.push()

app = Flask(__name__)

@app.route('/')
def index():
    host = request.headers.get('Host')
    return f'<h1>The host for this page is {host}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

