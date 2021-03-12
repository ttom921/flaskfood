from gevent.monkey import patch_all; patch_all()
import logging
from flask import Flask

from flask_uwsgi_websocket import WebSocket
from flask_uwsgi_websocket import GeventWebSocket


from api.example import example
from api.kafka import kafka
from api.wsocket import wsocket

from api.app import appManager
#app = Flask(__name__,  instance_relative_config=True)
app = appManager.create_app()
print(f"after create app={id(app)}")
# 設定info的level
app.logger.setLevel(logging.DEBUG)
# 讀取設定檔
app.config.from_object('instance.default')
#print(f"instance.default=>{app.config}")
app.config.from_pyfile('hisharp.py')
#print(f"hisharp.py=>{app.config}")

try:
    #sockets = WebSocket(app)
    sockets = GeventWebSocket(app)
    #sockets.init_app(app)
    #print(dir(sockets))
    #print("-------------------------")
    
except Exception as e:
    print("Error: flask_uwsgi_websocket, {0}".format(e))

# 藍圖註冊
app.register_blueprint(blueprint=example, url_prefix='/{0}/example'.format(app.config['API_VERSION']))

app.register_blueprint(blueprint=kafka, url_prefix='/{0}/kafka'.format(app.config['API_VERSION']))

sockets.register_blueprint(blueprint=wsocket, url_prefix='/{0}/websocket/'.format(app.config['API_VERSION']))
#sockets.register_blueprint(wsocket.construct_blueprint(sockets), url_prefix='/{0}/websocket/'.format(app.config['API_VERSION']))

@app.route('/', methods=['GET'])
def _index():
    return "ok"



if __name__ == "__main__":
    app.run()

"""
查看
http://192.168.40.191/v0.6/example/index
"""