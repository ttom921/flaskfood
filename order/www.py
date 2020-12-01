from application import app
from web.controller.index import router_index

app.register_blueprint(router_index,url_prefix="/")