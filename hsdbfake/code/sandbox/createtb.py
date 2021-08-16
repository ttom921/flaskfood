# --------------路徑-------------------
import os
import sys
from os import path
# D: \Project\imooc\www\hsdbfake\code\run.py
sys.path.append(path.dirname(path.dirname((path.abspath(__file__)))))
# print(f"sys.path={sys.path}")
# --------------路徑-------------------
# 使用log
from libs.utility.logs import *
# 使用database
from database import *

LOG_LEVEL_INFO()
# LOG_LEVEL_ERROR()
logging.info(f"start create tb")


SQLALCHEMY_BINDS_COMPANY = "mysql+pymysql://hisharp:Hisharp6f@192.168.40.209:3307/"
DB_ENGINE_ECHO = False

db.add_database("ttomdb", SQLALCHEMY_BINDS_COMPANY + "ttomdb", DB_ENGINE_ECHO)
# dbengine = db.get_engine("ttomdb")
# logging.info(f"dbengine=${dbengine}")


def init_db():
    logging.info(f"create tb")
    res = db.get_engine("ttomdb")
    Base.metadata.create_all(bind=res[1])


def drop_db():
    logging.info(f"drop tb")
    res = db.get_engine("ttomdb")
    Base.metadata.drop_all(bind=res[1])


init_db()
# drop_db()


# //--------------------------------
# engine = create_engine(SQLALCHEMY_BINDS_COMPANY + "ttomdb?charset=utf8", echo=DB_ENGINE_ECHO)
# logging.info(f"org engine=${engine}")


# def init_db():
#     Base.metadata.create_all(engine)


# def drop_db():
#     Base.metadata.drop_all(engine)


# Session = sessionmaker(bind=engine)
# session = Session()
# init_db()
