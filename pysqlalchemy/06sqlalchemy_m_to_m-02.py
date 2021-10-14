
# 由於此時是基於pymysql組件進行了MySQL數據庫的開發操作，所以一定要保証環境下有pymysql模塊
import sqlalchemy  # pip3 install SQLAlchemy
import sqlalchemy.ext.declarative  # 父類的結構定義
import sqlalchemy.orm  # ORM的所有工具
import sqlalchemy.orm.session  # 數據庫操作的核心
import datetime  # ORM組件要使用具體的日期類型
import random

import traceback
import pymysql
from libs.utility import *


# 加入訊息輸出
LOG_LEVEL_INFO()

# 定義MySQL數據庫方言（直接在連接上通過字符串的形式定義了）以及連接地址
MYSQL_URL = "mysql://hisharp:Hisharp6f@192.168.40.155:3306/ttomdb?charset=utf8"
# Base類型:sqlalchemy.orm.decl_api.DeclarativeMeta

Base = sqlalchemy.ext.declarative.declarative_base()  # 定義ORM映射父類

user_role = sqlalchemy.Table("user_role", Base.metadata,
                             sqlalchemy.Column("uid", sqlalchemy.String, sqlalchemy.ForeignKey("user.uid"), nullable=False, primary_key=True),
                             sqlalchemy.Column("rid", sqlalchemy.String, sqlalchemy.ForeignKey("role.rid"), nullable=False, primary_key=True)
                             )


class User(Base):
    __tablename__ = "user"
    uid = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    roles = sqlalchemy.orm.relationship("Role", secondary=user_role, backref="user")

    def __repr__(self) -> str:
        return f"用戶ID:{self.uid}、姓名:{self.name}"


class Role(Base):
    __tablename__ = "role"
    rid = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self) -> str:
        return f"角色ID:{self.rid}、名稱:{self.title}"


def main():

    try:
        engine = sqlalchemy.create_engine(MYSQL_URL, echo=True)  # 返回所有的操作信息
        sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 創建Session類型
        session = sqlalchemy.orm.session.Session()  # 實例化Session對象
        user = session.query(User).get("yootk")  # 獲取用戶信息
        logging.info(f"user=>{user}")
        for role in user.roles:
            logging.info(f"{role}")
        session.close()  # 持久態轉為游離態

    except Exception as e:
        logging.info(traceback.format_exc())


if __name__ == "__main__":  # 判斷程序執行名稱
    main()
