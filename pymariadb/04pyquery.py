import traceback
import pymysql
from libs.utility import *

# 加入訊息輸出
LOG_LEVEL_INFO()

# 傳統的pymysql組綿支持的是原生的SQL
SQL = "SELECT uid,name,age,birthday,salary,note FROM user"


def main():
    conn = None
    try:
        # 數據庫連接
        conn = pymysql.connect(host="192.168.40.209", port=3307, charset="UTF8", user="hisharp", password="Hisharp6f", database="ttomdb")
        cmd = conn.cursor()  # 獲得一個數據庫的操作對象
        cmd.execute(SQL)  # 執行SQL語句
        for user_row in cmd.fetchall():  # 返回查詢結果
            uid = user_row[0]
            name = user_row[1]
            age = user_row[2]
            birthday = user_row[3]
            salary = user_row[4]
            note = user_row[5]
            logging.info(f"用戶ID:{uid} 姓名:{name} 年齡:{age} birthday:{birthday} salary:{salary} note:{note}")
    except Exception as e:
        logging.info(traceback.format_exc())
    finally:
        conn.close()  # 數據為資源操倫，資源操作最後必須關畢


if __name__ == "__main__":  # 判斷程序執行名稱
    main()
