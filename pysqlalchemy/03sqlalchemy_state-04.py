
# 由於此時是基於pymysql組件進行了MySQL數據庫的開發操作，所以一定要保証環境下有pymysql模塊
import sqlalchemy  # pip3 install SQLAlchemy
import sqlalchemy.ext.declarative  # 父類的結構定義
import sqlalchemy.orm  # ORM的所有工具
import sqlalchemy.orm.session  # 數據庫操作的核心
import datetime  # ORM組件要使用具體的日期類型

import traceback
import pymysql
from libs.utility import *

# 加入訊息輸出
LOG_LEVEL_INFO()

# 定義MySQL數據庫方言（直接在連接上通過字符串的形式定義了）以及連接地址
MYSQL_URL = "mysql://hisharp:Hisharp6f@192.168.40.155:3306/ttomdb?charset=utf8"
# Base類型:sqlalchemy.orm.decl_api.DeclarativeMeta


class User(sqlalchemy.ext.declarative.declarative_base()):  # sqlalchemy.orm.decl_api.Base
    __tablename__ = "user"  # 數據表名稱
    uid = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)  # 屬性與字段映射
    name = sqlalchemy.Column(sqlalchemy.String)  # 映射字段
    age = sqlalchemy.Column(sqlalchemy.SMALLINT)  # 映射age字段
    birthday = sqlalchemy.Column(sqlalchemy.Date)  # 映射birthday字段
    salary = sqlalchemy.Column(sqlalchemy.Float)  # 映射salary字段
    note = sqlalchemy.Column(sqlalchemy.String)  # 映射note字段

    def __repr__(self) -> str:
        return f"用戶編號:{self.uid}, 姓名:{self.name}, 年齡:{self.age} ,生日:{self.birthday} ,月薪:{self.salary} ,備註:{self.note}"


def main():

    try:
        engine = sqlalchemy.create_engine(MYSQL_URL, echo=True)  # 返回所有的操作信息
        sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 創建Session類型
        session = sqlalchemy.orm.session.Session()  # 實例化Session對象
        user_a = session.query(User).get(1)  # 根據ID查詢
        user_a.name = "[程序修改]沐言優拓職業教育"  # 修改持久態下的數據
        user_b = session.query(User).get(1)  # 根據ID查詢
        user_b.age = 99  # 修改持久態下的數據

        logging.info(f"user_a={user_a}")
        logging.info(f"user_b={user_b}")
        session.close()  # 斷開了數據庫的連接
        user_c = session.query(User).get(1)  # 根據ID查詢
        logging.info(f"user_c={user_c}")

        session.close()  # 關畢session（釋放連接）
    except Exception as e:
        logging.info(traceback.format_exc())


if __name__ == "__main__":  # 判斷程序執行名稱
    main()
