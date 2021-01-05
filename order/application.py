from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os
from flask_sockets import Sockets


class Application(Flask):
    def __init__(self,import_name):
        super(Application,self).__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')
        # data=os.environ
        # print(data)
        # if "ops_config" in os.environ:
        #     self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])
        self.config.from_pyfile('config/%s_setting.py' % 'local')

        db.init_app(self)
        
db = SQLAlchemy()
app = Application(__name__)

manager = Manager(app)
sockets = Sockets(app)



