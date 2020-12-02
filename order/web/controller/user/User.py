
from flask import Blueprint,make_response,jsonify

router_user = Blueprint('user_page',__name__)

@router_user.route("/login")
def login():
    return make_response(jsonify("login"), 200)