import logging
import json
import socket
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
                    # datefmt='%m-%d %H:%M',
                    )
# logging.info(f"info")
# logging.debug(f"debug")
HOST = '192.168.83.129'
PORT = 5044


# def sendtcplog():
#     s = socket.socket()
#     while True:
#         str = input("S: ")
#         s.sendall(str.encode())
#         if(str == "Bye" or str == "bye"):
#             break

#     s.close()


def heartbeattcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    outdata = f'heartbeat'
    logging.info(f"send:{outdata}")
    s.send(outdata.encode())
    s.close()


def hearbeatloop():
    while True:
        heartbeattcp()
        time.sleep(1)


if __name__ == "__main__":
    # sendtcplog()
    hearbeatloop()
