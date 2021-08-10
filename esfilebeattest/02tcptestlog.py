import logging
import json
import socket
import time
import datetime  # 引入datetime
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
                    # datefmt='%m-%d %H:%M',
                    )
# logging.info(f"info")
# logging.debug(f"debug")
HOST = '192.168.83.129'
PORT = 9000


def heartbeattcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    nowTime = datetime.datetime.now()  # 取得現在時間
    sendmessage = f"[{nowTime}] ERROR, ClientIP:123.128.251.73, SeverIP:172.16.152.104, testmessage[測試訊息]#逃避雖可恥但有用#新垣結衣我老婆"
    # sendmessage = "[2016-12-10 23:59:59.634] ERROR, ClientIP:123.128.251.73, SeverIP:172.16.152.104, testmessage[測試訊息]#逃避雖可恥但有用#新垣結衣我老婆"
    outdata = f'{sendmessage}'
    logging.info(f"send:{outdata}")
    s.send(outdata.encode())
    s.close()


def hearbeatloop():
    while True:
        heartbeattcp()
        time.sleep(1)


if __name__ == "__main__":
    hearbeatloop()
