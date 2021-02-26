# #from  application.application import Application
# # import time

# # if __name__ == '__main__':
# #     import os
# #     if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
# #         print(time.time())
# #     myapp=Application.get_app()
# #     print("run.py->myapp={0}",id(myapp))
# #     myapp.run(debug=True)

# # from app import create_app
# import time
# #app = create_app()
# from application import app
# if __name__ == "__main__":
#     print("run*********",time.time())
#     app.run(host='0.0.0.0',debug='True',gevent=100)

# from flask import Flask,current_app

# app=Flask(__name__)

# if __name__== '__main__':
#     with app.app_context():
#         import a
#         import b
#         app.run(host='0.0.0.0',debug='True')

from flask import Flask,current_app
from flask_uwsgi_websocket import WebSocket
from flask_uwsgi_websocket import GeventWebSocket
from create import create_app 

app = create_app()
# # iniit app
# app = Flask(__name__)

# try:
#     sockets = GeventWebSocket(app=app)
# except Exception as e:
#     print("Error: flask_uwsgi_websocket, {0}".format(e))

# app.config['SECRET_KEY']="akjskldjf"
# with app.app_context():
    
#     # 藍圖註冊
#     from api.index.Index import router_index
#     from api.wsocket.Wsocket import router_websocket

#     app.register_blueprint(router_index)
#     sockets.register_blueprint(router_websocket,url_prefix='/{0}/ws'.format("v0.0"))

if __name__== '__main__':
    app.run(host='0.0.0.0',debug='True',gevent=100)
    # with app.app_context():
    #     app2=current_app
    #     app2.run(host='0.0.0.0',debug='True',gevent=100)

