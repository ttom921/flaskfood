import gevent.monkey
gevent.monkey.patch_all()
from flask import Flask, jsonify
from time import sleep



app = Flask(__name__)
# app.debug = True


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
    app.run()
