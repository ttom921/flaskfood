from application import app
from flask import request


@app.before_request
def before_request():
    path= request.path
    check_login()

'''
判斷用戶是否已經登錄
'''
def check_login():
    #app.logger.info("headers={}".format(request.headers))  
    token = request.headers.get('Authorization')
    app.logger.info("token={}".format(token))    
