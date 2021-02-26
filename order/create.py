from flask import Flask
from flask_uwsgi_websocket import WebSocket
from flask_uwsgi_websocket import GeventWebSocket


def create_app():
    # iniit app
    app = Flask(__name__)
    app.config['SECRET_KEY']="akjskldjf"

    try:
        sockets = GeventWebSocket(app=app)
    except Exception as e:
        print("Error: flask_uwsgi_websocket, {0}".format(e))

    

    with app.app_context():
        
        # 藍圖註冊
        from api.index.Index import router_index
        from api.wsocket.Wsocket import router_websocket


        app.register_blueprint(router_index)
        sockets.register_blueprint(router_websocket,url_prefix='/{0}/ws'.format("v0.0"))
    return app    