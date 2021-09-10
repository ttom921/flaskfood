import traceback
import pymysql
from libs.utility import *

# 加入訊息輸出
LOG_LEVEL_INFO()


# 傳統的pymysql組件支持的是原生的SQL
#SQL = "INTO user(name,age,birthday,salary,note) VALUES ('%s','%s','%s','%s','%s')" % (name,age,birthday,salary,note)
SQL_A = f"INSERT user(name, ,note) VALUES ('小李','www.example.com')"

# 以下這個會有exception
SQL_B = f"INSERT user(name, ,note) VALUES ('Mr'Yootk','www.example.com')"
SQL_C = f"INSERT user(name, ,note) VALUES ('小沐','www.example.com')"


def main():
    conn = None
    try:
        # 數據庫連接
        conn = pymysql.connect(host="192.168.40.209", port=3307, charset="UTF8", user="hisharp", password="Hisharp6f", database="ttomdb")
        cmd = conn.cursor()  # 獲得一個數據庫的操作對象
        cmd.execute(query=SQL_A)  # 執行SQL語句
        cmd.execute(query=SQL_B)  # 執行SQL語句
        cmd.execute(query=SQL_C)  # 執行SQL語句
        conn.commit()  # 提交事務

    except Exception as e:
        conn.rollback()  # 事務回滾
        logging.info(traceback.format_exc())
    finally:
        conn.close()  # 數據為資源操倫，資源操作最後必須關畢


if __name__ == "__main__":  # 判斷程序執行名稱
    main()
