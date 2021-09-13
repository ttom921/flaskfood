import traceback
import pymysql
import dbutils.pooled_db  # pip3 install DBUtils
from libs.utility import *

# 加入訊息輸出
LOG_LEVEL_INFO()


# 傳統的pymysql組件支持的是原生的SQL
SQL = f"INSERT INTO user(name, note) VALUES ('小李老師','www.example.com')"


def main():
    # conn = None
    try:
        pool = dbutils.pooled_db.PooledDB(
            creator=pymysql,  # 連接池管理的是pymysql的操作類型
            mincached=2,  # 空閒時維持2個連接
            maxcached=5,  # 空閒時鬼超𠯶5個連接
            maxconnections=20,  # 最大的連接數(測試)
            blocking=True,  # 引入阻塞隊列
            host="192.168.40.155",  # 主機
            port=3306,  # 端口
            user="hisharp",  # 用戶
            password="Hisharp6f",  # 密碼
            database="ttomdb",  # 數據庫
            charset="UTF8"  # 字符編碼
        )
        conn = pool.connection()  # 獲取數據庫連托
        cmd = conn.cursor()  # 獲得一個數據庫的操作對象
        cmd.execute(query=SQL)  # 執行SQL語句
        conn.commit()  # 提交事務

    except Exception as e:
        conn.rollback()  # 事務回滾
        logging.info(traceback.format_exc())
    finally:
        conn.close()  # 數據為資源操倫，資源操作最後必須關畢


if __name__ == "__main__":  # 判斷程序執行名稱
    main()
