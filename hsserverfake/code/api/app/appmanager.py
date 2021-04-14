from flask import Flask


class AppManager():

    def __init__(self):
        print(f"init AppManager")
        self.app = self.app = Flask(__name__, instance_relative_config=True)
        self.users = {}
        print(f"init AppManager app={id(self.app)}")

    def create_app(self):
        print(f"create_app app={id(self.app)}")
        return self.app


appManager = AppManager()
