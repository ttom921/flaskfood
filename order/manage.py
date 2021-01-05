from application import app,manager
from flask_script import Server
import www #引入

## web server
#manager.add_command("runserver",Server(host='0.0.0.0',port=app.config['SERVER_PORT'],use_debugger=True,use_reloader=True))
#manager.add_command("runserver",runserver_gevent)

##
@manager.command 
def runserver():
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    import logging
    logging.basicConfig(level=logging.DEBUG)
    app.debug = True
    server = pywsgi.WSGIServer(('', 5000),application=app, handler_class=WebSocketHandler,log=app.logger)
    try:
         server.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        if server.started:
            server.stop()
   

def main():
    #app.run(host='0.0.0.0',debug='True')
    #app.run(debug='True')
    #from gevent import pywsgi
    #from geventwebsocket.handler import WebSocketHandler
    #server = pywsgi.WSGIServer(('0.0.0.0', 8540), manager, handler_class=WebSocketHandler)
    manager.run()
    #server.serve_forever()
   

if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()