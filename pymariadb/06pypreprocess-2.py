import traceback
import pymysql
from libs.utility import *

# 加入訊息輸出
LOG_LEVEL_INFO()


name = "Mr'Yottk"  # 模擬鍵盤輸入
age = 16  # 模擬鍵盤輸入
birthday = "2016-06-28"  # 模擬鍵盤輸入
salary = 6000.00  # 模擬鍵盤輸入
note = "wwww.example.com"
# 傳統的pymysql組件支持的是原生的SQL
SQL = "INSERT INTO user(name,age,birthday,salary,note) VALUES (%s, %s, %s, %s, %s)"

logging.info(f"SQL ={SQL}")


def main():
    conn = None
    try:
        # 數據庫連接
        conn = pymysql.connect(host="192.168.40.155", port=3306, charset="UTF8", user="hisharp", password="Hisharp6f", database="ttomdb")
        cmd = conn.cursor()  # 獲得一個數據庫的操作對象
        cmd.execute(query=SQL, args=[name, age, birthday, salary, note])  # 執行SQL語句
        conn.commit()  # 提交事務
        logging.info(f"更新影響數據行數: {cmd.rowcount}")
        logging.info(f"最後一次增長ID: {cmd.lastrowid}")
    except Exception as e:
        logging.info(traceback.format_exc())
    finally:
        conn.close()  # 數據為資源操倫，資源操作最後必須關畢


if __name__ == "__main__":  # 判斷程序執行名稱
    main()
