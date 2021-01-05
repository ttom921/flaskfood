from flask import Flask,request
from flask_socketio import SocketIO,send, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# @socketio.on('connect', namespace='/test')
# def test_connect():
#     print('onconnect:')
#     emit('my response', {'data': 'Connected'})

# @socketio.on('disconnect', namespace='/test')
# def test_disconnect():
#     print('Client disconnected')


# @socketio.on('message')
# def handle_message(message):
#     print('received message: ' + message)
#     send(message, namespace='/test')  

# if __name__ == '__main__':
#     socketio.run(app, host='0.0.0.0',port=5000, debug=True)

@socketio.on("connect")
def onconnect():
    # socket id
    currentSocketId = request.sid
    # socketio namespace
    print(request.namespace)
    print("[server]<connect> socket.id=%s" % (currentSocketId))


@socketio.on("connected")
def onConnected(data):
    currentSocketId = request.sid
    print("[server]<connected> socket.id=%s msg=%s" %
          (currentSocketId, data))


@socketio.on("disconnect")
def ondisconnect():
    print("[server]<disconnect>")


@socketio.on("chatmessage")
def onchatmessage(data):
    msg = "[server]<chatmessage>:%s" % (data)
    print("[server]<chatmessage>:%s", msg)
    ## emit("chatmessage", data)
    ## emit("chatmessage", data, broadcast=True)
    emit("chatmessage", data, broadcast=True, include_self=False)


if __name__ == "__main__":
    app.debug = True  # vscode 才可以偵錯
    socketio.run(app,host='0.0.0.0', port=5000)

  

