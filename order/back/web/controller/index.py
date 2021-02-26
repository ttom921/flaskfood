from flask import Blueprint
import datetime 
router_index = Blueprint('index_page',__name__)

@router_index.route("/")
def index():
    return "Hello World {0}".format(datetime.datetime.now())