from flask import Flask,url_for,jsonify
from imooc import route_imooc

from common.libs.UrlManager import UrlManager
from flask_sqlalchemy import SQLAlchemy

API_VERSION="v0.0"
app = Flask(__name__)

# 資料庫相關
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://imooc:12345678@127.0.0.1:3306/mysql"
db=SQLAlchemy(app)

app.register_blueprint(route_imooc,url_prefix='/{0}/api/imooc'.format(API_VERSION))

@app.route("/v0.0/")
def v0_0index():
    url = url_for("hello_world")
    url1_1= UrlManager.buildUrl("/v0.0/api")
    msg =  "hello world url=%s , url1_1=%s " %(url,url1_1)
    app.logger.debug(msg)
    app.logger.warning(msg)
    app.logger.error(msg)   
    return msg

@app.route("/v0.0/api/")
def hello_world():
    from sqlalchemy import text
    sql= text("SELECT * from `user`")
    result = db.engine.execute(sql)
    for row in result:
        app.logger.info(row)
    return "Hello world /v0.0/api"

@app.route("/v0.0/api/movies/")
def get_movies_api():
    movies=[{'name':'刺激1995'},{'name':'教父'}]
    return jsonify(movies) 

# 找不到網頁的error handler
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.run( debug=True)