import traceback
import pymysql
from libs.utility import *

# 加入訊息輸出
LOG_LEVEL_INFO()


def main():
    conn = None
    try:
        conn = pymysql.connect(host="192.168.40.209", port=3307, charset="UTF8", user="hisharp", password="Hisharp6f", database="ttomdb")
        # logging.info('logging.info: Hello info!')
        logging.info(f"mariadb 連接成功 目前數據庫版本為: {conn.get_server_info()}")
        logging.info(f"mariadb 連接成功 事務提交模式: {conn.get_autocommit()}")
    except Exception as e:
        logging.info(traceback.format_exc())
    finally:
        conn.close()


if __name__ == "__main__":  # 判斷程序執行名稱
    main()
