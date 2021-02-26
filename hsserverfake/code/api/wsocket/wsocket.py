from flask import Blueprint, request, current_app as app, jsonify, g
import datetime
import time
import json
from geventwebsocket import WebSocketError


users = {}
def construct_blueprint(arg1):
    wsocket = Blueprint(name="wsocket", import_name=__name__)

    @wsocket.route("/echo")
    def _echo_socket(ws):
        #print(dir(arg1))
        #print(dir(arg1.app))
        #print(id(arg1.app))
        # arg1.app.logger.debug('logging.debug: Hello debug!')
        # arg1.app.logger.info('logging.info: Hello info!')
        # arg1.app.logger.warning('logging.warning: Hello warning! debugFaile')
        # arg1.app.logger.error('logging.error: Hello error!')
        # arg1.app.logger.critical('logging.critical: Hello critical!')
        # with arg1.app.app_context():
        #     arg1.app.logger.info('socket={0}'.format(ws))
        #     #print(arg1.app.config)
        #arg1.app.logger.info(f"{dir(ws)}")
        # 加入列表
        users[ws.id] = ws
        arg1.app.logger.info(f"加入列表={ws.id}")
        arg1.app.logger.info(f"列表={users}")
        while ws.connected :
            time.sleep(1)
            #arg1.app.logger.info(f"===============wsocket.route=============")
            try:
                recdata=ws.receive()
                #len(recdata)
                #app.logger.info('reclent={0}'.format(len(recdata)))
            except WebSocketError:
                break
            if recdata is not None:     
                if len(recdata) == 0:
                    continue  
                msg=json.loads(recdata)  
                arg1.app.logger.info(f"現有連接用戶：{len(users)}") 
                arg1.app.logger.info(f"服務器收到 data={msg}")
                if msg:
                    now = datetime.datetime.now()
                    sendmsg=f"{msg['message']} {now}"
                    msg['message']=sendmsg
                    sendata=json.dumps(msg)
                    #print(f'服務器 傳送:{sendata}')
                    for id in users:
                        try:
                            arg1.app.logger.info(f"送給{users[id].id} {sendata}")
                            users[id].send(sendata)
                        except WebSocketError:
                            print('用戶已斷開連接')
                    # for client in client_dict.values():
                    #     try:
                    #         arg1.app.logger.info(f"送給{client} {sendata}")
                    #         client.send(sendata)
                    #     except WebSocketError:
                    #         print('用戶已斷開連接')
            else:
                break

        #close wesocket
        arg1.app.logger.info(f'關畢 socket={ws.id}')
        del users[ws.id] 

    return(wsocket)

# wsocket = Blueprint(name="wsocket", import_name=__name__)



# '''
# 以下開始API實作
# '''

# @wsocket.route("/echo")
# def _echo_socket(ws):
#     #print(dir(current_app))
#     global GLOBAL_app
#     print(ws)
#     print(request)
#     print(g)
#     # print(dir(ws))
#     #print(dir(wsocket))
#     #     #wsock = request.environ.get('wsgi.websocket')
#     #     #取得wsocke和socket是一樣的
#     #     #app.logger.info('socket={0}'.format(socket))
#     #     app.logger.info('socket={0}'.format(dir(socket)))
#     #     # recdata=socket.receive()
#     #     # msg=json.loads(recdata)
#     #     # name=msg['author']