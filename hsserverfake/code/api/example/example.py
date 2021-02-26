from flask import Blueprint,request,make_response,jsonify

#example = Blueprint('index_page',__name__)
example = Blueprint(name="example", import_name=__name__)


@example.route("/index",methods=["GET"])
def _index():
    return "example index"