from application import app,manager
from flask_script import Server

import www #引入

## web server
manager.add_command("runserver",Server(host='127.0.0.1',port=app.config['SERVER_PORT'],use_debugger=True,use_reloader=True))

def main():
    #app.run(host='0.0.0.0',debug='True')
    #app.run(debug='True')
    manager.run();

if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()