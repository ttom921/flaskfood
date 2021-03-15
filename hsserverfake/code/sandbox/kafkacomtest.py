
import json
import os
import sys
import time
from pathlib import Path
from os import path

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


import coloredlogs
from libs.utility import *

from kafka.errors import KafkaError
from kafka import KafkaConsumer

LOG_LEVEL_INFO()
# LOG_LEVEL_DEBUG()
# LOG_LEVEL_ERROR()

# 參數設定
__filename__ = os.path.split(__file__)[-1]


# 檢查檔案目前檔案是否正在執行
def isRuning():
    if checkIfRunning(__filename__, os.getpid()) is True:
        print("---- %s 重複執行 ----" % __filename__)
        print("---- %s 重複執行 ----" % os.getpid())
        exit(0)


def readServerConfig():
    config = str(Path(__file__).absolute()).split("/")
    # logging.info(f"config={config}")
    del config[-1]
    # logging.info(f"config={config}")
    __configPath__ = f"{'/'.join(map(str,config))}/config/server_config.json"
    # logging.info(f"__configPath__={__configPath__}")
    server_config = json.loads(open(__configPath__).read())
    # logging.info(f"server_config={server_config}")
    return server_config


def main():
    # 檢查檔案目前檔案是否正在執行
    isRuning()
    # 讀取config檔
    server_config = readServerConfig()
    logging.info(f"server_config={server_config}")
    topic = "newtopic"
    consumer = None
    try:
        consumer = KafkaConsumer(topic,
                                 bootstrap_servers=server_config["KFKA_URL"])

        for msg in consumer:
            print(msg)
            print(f"topic = {msg.topic}")  # topic default is string
            print(f"partition = {msg.partition}")
            print(f"offset = {msg.offset}")
            print(f"value = {msg.value.decode('utf-8')}")
            print(f"timestamp = {msg.timestamp}")

    except KafkaError as ke:
        # producer.close()
        logging.info(f"{ke.errno}-{ke.message}")
    except Exception as e:
        # producer.close()
        logging.info(f"exception ={e}")
    except KeyboardInterrupt as e:
        logging.info(f"KeyboardInterrupt ={e}")
    finally:
        logging.info(f"=====================finally ================")
        consumer.close()


if __name__ == "__main__":
    main()
