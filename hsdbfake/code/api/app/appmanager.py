from flask import Flask

# 建立Flask的app的管理者


class AppManager():
    def __init__(self):
        print(f"init AppManager")
        self.app = Flask(__name__, instance_relative_config=True)
        print(f"init AppManager app={id(self.app)}")

    def create_app(self):
        print(f"create_app app={id(self.app)}")
        return self.app


appManager = AppManager()
