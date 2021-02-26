from flask import Blueprint,request
import datetime
import time
import json
from application import app
from werkzeug.exceptions import abort
from geventwebsocket import WebSocketError

router_websocket = Blueprint('websocket_page',__name__)

client_dict = {}

@router_websocket.route("/echo")
def echo_socket(socket):
    
    #wsock = request.environ.get('wsgi.websocket')
    #取得wsocke和socket是一樣的
    #app.logger.info('socket={0}'.format(socket))
    app.logger.info('socket={0}'.format(dir(socket)))
    # recdata=socket.receive()
    # msg=json.loads(recdata)
    # name=msg['author']
    # 加入列表
    client_dict[socket]=socket

    # if not socket:
    #     abort(400, 'Expected WebSocket request.')


    while True :
        time.sleep(1)
        try:
            recdata=socket.receive()
            #len(recdata)
            #app.logger.info('reclent={0}'.format(len(recdata)))
        except WebSocketError:
            break
       
        if len(recdata)==0:
            continue
        print("現有連接用戶：%s" % (len(client_dict))) 
        print(f'i received:{recdata}')
        msg=json.loads(recdata)
        #app.logger.info('type msg={0}'.format(type(msg))) 
        # message = socket.receive()
        # print(message)
        print(f'i convert received:{msg}')
        if msg:
            now = datetime.datetime.now()
            sendmsg='{} {}'.format(msg['message'],now)
            msg['message']=sendmsg
            sendata=json.dumps(msg)
            print(f'i sent:{sendata}')
            for client in client_dict.values():
                try:
                    client.send(sendata)
                except WebSocketError:
                    print('用戶已斷開連接')
    #close wesocket
    app.logger.info('close socket={0}'.format(socket))
    client_dict.pop(socket)        
            


        