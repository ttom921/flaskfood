from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, BigInteger
from .base import Base
from datetime import date, datetime
from database import *


# from libs.utility.logs import *
# LOG_LEVEL_INFO()


class Stock(Base):
    """定義數據模型"""
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True)
    code = Column(String(4), nullable=True)
    name = Column(String(32), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    def __init__(self, code="-1", name="uname"):
        print("__init__ stock")
        self.code = code
        self.name = name

    def __repr__(self):
        return f'<Stock {self.id}>'
