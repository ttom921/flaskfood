from flask import Blueprint
import datetime

router_index = Blueprint('index_api',__name__)
@router_index.route("/")
def index():
    return "Hello World {0}".format(datetime.datetime.now())