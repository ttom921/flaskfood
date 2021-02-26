#!/usr/bin/env python
from flask import Flask, render_template, request
from flask_uwsgi_websocket import GeventWebSocket

app = Flask(__name__)
ws = GeventWebSocket(app)

@app.route('/')
def index():
    return "hello websocket"

@ws.route('/websocket')
def echo(ws):
    print("WWWWWWWWWWWWWWWWWWWWWW")
    
    while True:
        msg = ws.receive()
        print(msg)
        if msg is not None:
            ws.send(msg)
        else: return

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, gevent=100)
