
from flask import Blueprint,request,make_response,jsonify
from application import app
import json
router_user = Blueprint('user_page',__name__)

@router_user.route("/login",methods=["GET","POST"])
def login():
    # 目前login方法用不到
    if request.method == "GET":
        app.logger.debug("GET")
        return make_response(jsonify("login get"), 200)

    # if request.method == "POST":
    #     return make_response(jsonify("用戶登入"), 200) 
    # 取值
    if request.method =="POST":
        #app.logger.debug("POST")
        #取得JSON的值因為angular是這樣傳值的
        data = json.loads(request.data)
        app.logger.debug(data)
        #req= request.values
        login_name = data['login_name'] if 'login_name' in data else ''  
        login_pwd = data['login_pwd'] if 'login_pwd' in data else ''
        resmsg="%s-%s" % (login_name,login_pwd)
        app.logger.debug(resmsg)
        return make_response(jsonify(resmsg),200)  