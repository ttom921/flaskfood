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


@example.route("add", methods=["GET"], endpoint='example_add')
@flask_request_initial
def _add(reqArgs):
    session = g.ttomdb_session
    try:
        # # 建立整一筆資料
        # logging.info(f"add g.ttomdb_session={g.ttomdb_session}")
        # status, dbsession = db.get_session("ttomdb")
        # logging.info(f"example->_add -> dbsession_session={dbsession}")

        # 建立第一筆資料
        stock = Stocks()
        stock.code = '1101'
        stock.name = '台泥'
        session.add(stock)

        # 建立第二筆資料
        stock = Stocks()
        stock.code = '1102'
        stock.name = '亞泥'
        session.add(stock)

        # 建立第三筆資料
        stock = Stocks()
        stock.code = '1103'
        stock.name = '嘉泥'
        session.add(stock)

        # 建立第四筆資料
        stock = Stocks()
        stock.code = '1201'
        stock.name = '味全'
        session.add(stock)

        # mystock = session.query(Stocks).filter_by(code="1101").first()
        # logging.info(f"mystock={mystock}")
        # 寫入資料庫
        session.commit()
        session.remove()
        return '新增資料 OK'
    except Exception as e:
        # 發生例外錯誤，還原交易
        session.rollback()
        session.remove()
        logging.error('新增資料失敗')
        logging.error(e)
        return "新增資料失敗"


@example.route("batadd", methods=["GET"], endpoint='example_batadd')
@flask_request_initial
def _batadd(reqArgs):
    session = g.ttomdb_session
    try:
        for i in range(100):
            stock = Stocks()
            stock.code = f"cd{i}"
            stock.name = f"name {i}"
            # if i == 50:
            #     raise 'test db roback'
            session.add(stock)
        # 寫入資料庫
        session.commit()
        return "bat add ok"
    except Exception as e:
        # 發生例外錯誤，還原交易
        session.rollback()
        logging.error(f'e=>{e}')
        return "bat add faile"


@example.route("clear", methods=["GET"], endpoint='example_clear')
@flask_request_initial
def _clear(reqArgs):
    session = g.ttomdb_session
    try:
        # 執行原生 SQL 命令清空資料庫
        session.execute('TRUNCATE TABLE stocks')
        # 送出執行命令
        session.commit()
        return "清空資料 ok"
    except Exception as e:
        # 發生例外錯誤，還原交易
        # 測試完不能rollback
        # session.rollback()
        logging.error('清空資料失敗')
        return "清空資料失敗"
