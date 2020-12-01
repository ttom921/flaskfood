from flask import Blueprint

router_index = Blueprint('index_page',__name__)

@router_index.route("/")
def index():
    return "Hello World"