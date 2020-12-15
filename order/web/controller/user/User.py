
from flask import Blueprint,request,make_response,jsonify
import json
from common.models.User import User
from common.libs.user.UserService import UserService
from common.libs.response.RespCode import RespCode
from application import app

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
        #取得JSON的值因為angular是傳json值的
        data = json.loads(request.data)
        #app.logger.debug(data)
        # 返回值
        resp ={'code':200,'msg':'登錄成功','data':{}}
        login_name = data['login_name'] if 'login_name' in data else ''  
        login_pwd = data['login_pwd'] if 'login_pwd' in data else ''
        #resmsg="%s-%s" % (login_name,login_pwd)
        #app.logger.debug(resmsg)
        # return make_response(jsonify(resmsg),200)  
        # 檢查參數值
        if login_name is None or len(login_name) < 1 :
            resp['code']=RespCode.UNDEFINERROR
            resp['msg']="請輸入正確的登錄用戶名~~"
            app.logger.debug(resp)
            return resp['msg'],resp['code']
            
        if login_pwd is None or len(login_pwd) <1:
            resp['code']=RespCode.UNDEFINERROR
            resp['msg']="請輸入正確的登錄密碼~~"
            return resp['msg'],resp['code']

        # 資料庫相關
        user_info = User.query.filter_by( login_name= login_name).first()
        if not user_info:
            resp['code']=RespCode.UNDEFINERROR
            resp['msg']="請輸入正確的用戶名和密碼-1~~"
            return resp['msg'],resp['code']

        # 檢查密碼
        if user_info.login_pwd != UserService.genePwd(login_pwd,user_info.login_salt):
           resp['code']=RespCode.UNDEFINERROR
           resp['msg'] ="請輸入正確的用戶名和密碼-2~~"
           return resp['msg'],resp['code']
        # 登入成功 時，返回 auth code 
        tokenData=dict()
        #tokenData["mooc_foo"]="%s#%s"%("aaaaa",user_info.uid)
        tokenData[app.config["AUTH_TOKEN_NAME"]]="%s#%s"%(UserService.geneAuthCode(user_info),user_info.uid)
        
        resp['data']=tokenData
        #return make_response(jsonify(resp),200)  
        return jsonify(resp)  

@router_user.route("/example",methods=["GET"])
def userexample():
    # 返回值
    resp ={'code':200,'msg':'測試成功','data':{}}
    return jsonify(resp)  