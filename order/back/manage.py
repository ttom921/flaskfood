#from application import app,manager
from application import app
#rom flask_script import Server
#import www #引入
from application import sockets

## web server
#manager.add_command("runserver",Server(host='0.0.0.0',port=app.config['SERVER_PORT'],use_debugger=True,use_reloader=True))
#manager.add_command("runserver",Server(use_debugger=True,use_reloader=True))
# @manager.command
# def runserver():
#     #app.run(debug='True')
#     #app.logger.info('----------------------------------')
#     #app.logger.info('runserver')
#     app.run(host='0.0.0.0',debug=app.config['DEBUG'])
# ##
 

# def main():
#     #app.run(host='0.0.0.0',debug='True')
#     #app.run(debug='True')
#     #app.logger.info('main')
#     manager.run()
print("---------------------------------")
print("mange.py->app={0}",id(app))
from web.controller.wsocket.wsocket import router_websocket
app.logger.info("---------藍圖功能------------")
#sockets.register_blueprint(router_websocket,url_prefix='/{0}/ws'.format(app.config['API_VERSION']))
sockets.register_blueprint(router_websocket,url_prefix='/{0}/ws'.format("v0.0"))
#藍圖功能，對所有的url進行藍圖功能配置
#    
if __name__ == '__main__':
    try:
        import sys
        #sys.exit(main())
        sys.exit(app.run(host='0.0.0.0',debug='True',gevent=100))
    except Exception as e:
        import traceback
        traceback.print_exc()
