
from flask import Blueprint,request,make_response,jsonify

router_user = Blueprint('user_page',__name__)

@router_user.route("/login",methods=["GET","POST"])
def login():
    # 目前login方法用不到
    if request.method == "GET":
        return make_response(jsonify("login get"), 200)

    if request.method == "POST":
        return make_response(jsonify("用戶登入"), 200)    