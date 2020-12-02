from application import app
from web.controller.index import router_index
from web.controller.user.User import router_user
#註冊api

#app.register_blueprint(router_index,url_prefix="/")
#app.register_blueprint(router_user,url_prefix = "/v0.0/user")
app.register_blueprint(router_index,url_prefix='/{0}/'.format(app.config['API_VERSION']))
app.register_blueprint(router_user,url_prefix='/{0}/user'.format(app.config['API_VERSION']))


