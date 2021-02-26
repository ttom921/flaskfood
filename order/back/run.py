#from application import app,manager
#from application import app
#import www #引入
from flask import Flask

from flask_uwsgi_websocket import WebSocket
from flask_uwsgi_websocket import GeventWebSocket

app = Flask(__name__,  instance_relative_config=True)


try:
    sockets = GeventWebSocket(app=app)
except Exception as e:
    print("Error: flask_uwsgi_websocket, {0}".format(e))


#藍圖功能，對所有的url進行藍圖功能配置
from web.controller.index import router_index
from web.controller.user.User import router_user
from web.controller.wsocket.wsocket import router_websocket
app.register_blueprint(router_index,url_prefix="/")
#app.register_blueprint(router_user,url_prefix = "/v0.0/user")
# app.register_blueprint(router_index,url_prefix='/{0}/'.format(app.config['API_VERSION']))
# app.register_blueprint(router_user,url_prefix='/{0}/user'.format(app.config['API_VERSION']))
app.logger.info("---------藍圖功能------------")
#sockets.register_blueprint(router_websocket,url_prefix='/{0}/ws'.format(app.config['API_VERSION']))
sockets.register_blueprint(router_websocket,url_prefix='/{0}/ws'.format("v0.0"))
#藍圖功能，對所有的url進行藍圖功能配置


#sockets.register_blueprint(blueprint=wsocket, url_prefix='/{0}/websocket/'.format(app.config['API_VERSION']))
if __name__ == '__main__':
    try:
        import sys
        #sys.exit(main())
        sys.exit(app.run(host='0.0.0.0',debug='True',gevent=100))
    except Exception as e:
        import traceback
        traceback.print_exc()
