from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_uwsgi_websocket import GeventWebSocket,WebSocket
import os



# class Application(Flask):
#     def __init__(self,import_name):
#         print("Application init--------------------")
#         print("Application init")
#         super(Application,self).__init__(import_name)
#         self.config.from_pyfile('config/base_setting.py')
#         # data=os.environ
#         # print(data)
#         # if "ops_config" in os.environ:
#         #     self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])
#         self.config.from_pyfile('config/%s_setting.py' % 'local')

#         db.init_app(self)
        
db = SQLAlchemy()
app = Flask(__name__,  instance_relative_config=True)
print("application.py-------------app={0}".format(id(app)))
#app = Application(__name__)

try:
    sockets = GeventWebSocket(app=app)
except Exception as e:
    print("Error: flask_uwsgi_websocket, {0}".format(e))

#manager = Manager(app)
#ockets = WebSocket(app)



