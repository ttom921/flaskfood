import traceback
import pymysql
from libs.utility import *

# 加入訊息輸出
LOG_LEVEL_INFO()

# 傳統的pymysql組綿支持的是原生的SQL
SQL = "UPDATE user SET name='周沐言' ,age=26 WHERE uid=2"


def main():
    conn = None
    try:
        conn = pymysql.connect(host="192.168.40.209", port=3307, charset="UTF8", user="hisharp", password="Hisharp6f", database="ttomdb")
        cmd = conn.cursor()  # 獲得一個數據庫的操作對象
        cmd.execute(SQL)  # 執行SQL語句
        conn.commit()  # 提交事務，如果不提事務，更新不生效
        logging.info(f"更新影響數據行數: {cmd.rowcount}")
    except Exception as e:
        logging.info(traceback.format_exc())
    finally:
        conn.close()  # 數據為資源操倫，資源操作最後必須關畢


if __name__ == "__main__":  # 判斷程序執行名稱
    main()
