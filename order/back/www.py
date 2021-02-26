from application import app
from application import sockets
#註冊攔劫器
from web.interceptors.AuthInterceptor import *
#註冊攔劫器



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

# @app.route("/")
# def hello_world():
#     return "Hello World"