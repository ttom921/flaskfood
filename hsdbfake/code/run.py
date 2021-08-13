# 使用log
from libs.utility.logs import *
from instance.autoconfig import *

# 使用database
from database import *

from api.app import appManager
from api.example import example

LOG_LEVEL_INFO()
# LOG_LEVEL_ERROR()
app = appManager.create_app()
logging.info(f"after create app={id(app)}")
# print(f"after create app={id(app)}")

# 讀取設定檔
# 預設的設定檔
app.config.from_object('instance.default')
# logging.info(f"from_object app.config={app.config}")
# 有修改的設定檔
app.config.from_pyfile(AUTO_CONFIG_FILE)
# logging.info(f"from_pyfile app.config={app.config}")

# 加入資料庫
with app.app_context():
    db.add_database("ttomdb", app.config["SQLALCHEMY_BINDS_COMPANY"] + "ttomdb", app.config['DB_ENGINE_ECHO'])


@app.teardown_appcontext
def shutdown_session(exception=None):

    status, dbSession = db.get_session("ttomdb")
    logging.info(f"shutdown_session status={status} dbSession={dbSession}")
    if dbSession is not None:
        dbSession.remove()
    status, dbengine = db.get_engine("ttomdb")
    # print(type(dbengine))
    # print(dir(dbengine))
    if dbengine is not None:
        dbengine.engine.dispose()


# 藍圖註冊
app.register_blueprint(blueprint=example, url_prefix='/{0}/example'.format(app.config['API_VERSION']))


@app.route('/', methods=['GET'])
def _index():
    return "ok"


if __name__ == "__main__":
    try:
        # print(f" app.run() app={id(app)}")
        logging.info(f"app.run()  app={id(app)}")
        app.run(host="0.0.0.0", debug=True)
    except Exception as e:
        print(str(e))

"""
查看
http://192.168.40.190:5000/
http://192.168.40.190:5000/v0.8/example/index
#http://192.168.40.190/v0.8/example/index
"""
