from flask import current_app as app
from libs.utility import *
from libs.headers import *

from flask import Blueprint, request, make_response, jsonify


from database import *


from libs.utility.logs import *
LOG_LEVEL_INFO()

example = Blueprint(name="example", import_name=__name__)


@example.route("index", methods=["GET"])
def _index():
    return "example index"


@example.route("add", methods=["GET"])
@flask_request_initial
def _add(reqArgs):
    try:
        # # 建立整一筆資料
        # logging.info(f"flask_request_initial -> current_app={id(app)}")
        # logging.info(f"flask_request_initial -> current_app={type(app)}")
        # logging.info(f"flask_request_initial -> current_app={dir(app)}")
        status, dbsession = db.get_session("ttomdb")
        logging.info(f"example->_add -> dbsession_session={dbsession}")
      # 建立第一筆資料
        stocks = Stocks()
        stocks.code = '1101'
        stocks.name = '台泥'
        logging.info(f"stock={stocks.code}")
        dbsession.add(stocks)

        mystock = dbsession.query(Stocks).filter_by(code="1101").first()
        logging.info(f"mystock={mystock}")
        # 寫入資料庫
        dbsession.commit()
        return 'OK'
    except Exception as e:
        # 發生例外錯誤，還原交易
        # session.rollback()
        logging.error('新增資料失敗')
        logging.error(e)
        return "新增資料失敗"
