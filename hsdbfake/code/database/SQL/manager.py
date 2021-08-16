from flask import Flask, _app_ctx_stack
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
# from libs.utility.logs import *

# LOG_LEVEL_INFO()


class dbmanager(object):
    __dbs = {}

    def add_database(self, key, url, echo):
        if key not in self.__dbs.keys():
            connstr = f"{url}?charset=utf8"
            # logging.info(f"add_database connstr={connstr} echo={echo}")
            engine = _EngineConnector(f"{connstr}")
            engine.create_engine(echo)
            self.__dbs[key] = engine

    def get_session(self, key):
        if key not in self.__dbs.keys():
            return False, None
        return True, self.__dbs[key].session

    def get_engine(self, key):
        if key not in self.__dbs.keys():
            return False, None
        return True, self.__dbs[key].engine

    def get_all_database_names(self):
        return self.__dbs.keys()


class _EngineConnector(object):
    def __init__(self, bind=None):
        self.engine = None
        self.bind = bind
        self.session = None

    def create_engine(self, echo):
        self.engine = create_engine(
            self.bind,
            pool_size=300,
            max_overflow=200,
            pool_recycle=7200,
            pool_pre_ping=True,
            echo=echo
        )
        SessionFactory = sessionmaker(bind=self.engine, autoflush=False)
        # SessionFactory = sessionmaker(bind=self.engine)
        # Base.metadata.create_all(bind=self.engine)
        # session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)
        session = scoped_session(SessionFactory, scopefunc=_app_ctx_stack.__ident_func__)
        self.session = session


db = dbmanager()
