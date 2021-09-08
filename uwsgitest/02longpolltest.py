from gevent.monkey import patch_all; patch_all()
from gevent.pywsgi import WSGIServer
from flask import Flask, jsonify
from time import sleep


app = Flask(__name__)
app.debug = True


@app.route('/long-polling')
def long_polling():
    i = 0
    while True:
        if i == 10:
            return jsonify({'error': 0})
        else:
            i += 1
            sleep(5)


if __name__ == '__main__':
    server = WSGIServer(('127.0.0.1', 5000), app)
    server.serve_forever()