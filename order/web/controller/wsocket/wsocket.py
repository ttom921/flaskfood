from flask import Blueprint
import datetime
import time
router_websocket = Blueprint('websocket_page',__name__)

@router_websocket.route("/echo")
def echo_socket(socket):
    while not socket.closed:
        msg = socket.receive()
        print(f'i received:{msg}')
        # message = socket.receive()
        # print(message)
        if msg:
            now = datetime.datetime.now()
            sendmsg='{} {}'.format(msg,now)
            socket.send(sendmsg)
            print(f'i sent:{sendmsg}')
            time.sleep(1)


        