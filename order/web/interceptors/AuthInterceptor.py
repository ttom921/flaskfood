from application import app
from flask import request
from common.models.User import User
from common.libs.user.UserService import UserService
from common.libs.response.RespCode import RespCode
import re

@app.before_request
def before_request():
    path= request.path
    # 返回值
    resp ={'code':200,'msg':'登錄成功','data':{}}

    #不用檢查
    ignore_urls= app.config['IGNORE_URLS']
    ignore_check_login_urls=app.config['IGNORE_CHECK_LOGIN_URLS']
    
    pattern=re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
       app.logger.info("match={}".format(ignore_check_login_urls)) 
       return  
   
   

    user_info=check_login()

    pattern=re.compile('%s' % "|".join(ignore_urls))
    #app.logger.info("pattern={}".format(pattern)) 
    #app.logger.info("path={}".format(path)) 
    if pattern.match(path):
        #app.logger.info("match={}".format(ignore_urls)) 
        #return resp['msg'],resp['code']  
        return

    if not user_info:
       resp['code']=RespCode.TOKEN_ERROR
       resp['msg']="Token 無法解析"
       return resp['msg'],resp['code']  

'''
判斷用戶是否已經登錄
'''
def check_login():
    #app.logger.info("headers={}".format(request.headers))  
    token_info = request.headers.get('Authorization')
    #app.logger.info("token={}".format(token_info)) 
    if token_info is None:
        return False   

    auth_info = token_info.split("#")
    if len(auth_info) !=2:
        return False

    try:
        user_info=User.query.filter_by( uid=auth_info[1]).first()    
    except Exception as e:
        app.logger.error(e)
        return False
    
    if user_info is None:
        return False

    if auth_info[0] != UserService.geneAuthCode(user_info):
        return False

    return user_info        