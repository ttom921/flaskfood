
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


class Company(Base):
    __tablename__ = "company"  # 映射表
    cid = sqlalchemy.Column(sqlalchemy.String, primary_key=True)  # company.cid 映射
    cname = sqlalchemy.Column(sqlalchemy.String)  # company.cname 映射
    site = sqlalchemy.Column(sqlalchemy.String)  # company.site 映射
    depts = sqlalchemy.orm.relationship("Dept", order_by="Dept.cid", backref="company")

    def __repr__(self) -> str:
        return f"公司編號:{self.cid},名稱:{self.cname},網址:{self.site}"


class Dept(Base):
    __tablename__ = "dept"  # 映射表
    did = sqlalchemy.Column(sqlalchemy.BIGINT, primary_key=True)
    dname = sqlalchemy.Column(sqlalchemy.String)
    cid = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("company.cid"))  # 外鍵關聯

    def __repr__(self) -> str:
        return f"部門編號:{self.did},名稱:{self.dname},公司編號:{self.cid}"


def main():

    try:
        engine = sqlalchemy.create_engine(MYSQL_URL, echo=True)  # 返回所有的操作信息
        sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 創建Session類型
        dept_list = [Dept(dname="軟件部"), Dept(dname="信息部"), Dept(dname="客服部")]  # 部門列表
        company = Company(cid="C-002", cname="沐言優拓", site="www.school.net", depts=dept_list)  # 構建Company對象
        session = sqlalchemy.orm.session.Session()  # 實例化Session對象
        session.add(company)  # 公司數據的保存
        session.commit()  # 持久態
        for dept in dept_list:
            logging.info(f"[新增部冊編號]did = {dept.did}")
        session.close()  # 關畢session（釋放連接）
    except Exception as e:
        logging.info(traceback.format_exc())


if __name__ == "__main__":  # 判斷程序執行名稱
    main()
