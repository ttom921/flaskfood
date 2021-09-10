import traceback
import pymysql
from libs.utility import *
# 加入訊息輸出
LOG_LEVEL_INFO()
# 傳統的pymysql組件支持的是原生的SQL
SQL = "INSERT INTO user(name,age,birthday,salary,note) VALUES (%s, %s, %s, %s, %s)"


def main():
    conn = None
    try:
        # 數據庫連接
        conn = pymysql.connect(host="192.168.40.155", port=3306, charset="UTF8", user="hisharp", password="Hisharp6f", database="ttomdb")
        cmd = conn.cursor()  # 獲得一個數據庫的操作對象
        data_list = []  # 創建一個列表
        for num in range(1001):
            data_list.append((f"沐言優拓 - {num}", 18, "2008-08-21", 5000.00, "www.example.com"))
            if num % 20 == 0:  # 每保存20條數據就進行更新
                cmd.executemany(query=SQL, args=data_list)
                data_list.clear()

        conn.commit()  # 提交事務
        logging.info(f"更新影響數據行數: {cmd.rowcount}")
        logging.info(f"最後一次增長ID: {cmd.lastrowid}")
    except Exception as e:
        logging.info(traceback.format_exc())
    finally:
        conn.close()  # 數據為資源操倫，資源操作最後必須關畢


if __name__ == "__main__":  # 判斷程序執行名稱
    main()
