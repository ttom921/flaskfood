# socket-tcp-client-heartbeat.py

import logging
from time import sleep
from datetime import datetime
import socket
# logging.basicConfig(level=logging.DEBUG)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
                    # datefmt='%m-%d %H:%M',
                    )

HOST = "192.168.40.191"
PORT = 8000

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpserver.connect((HOST, PORT))

while True:
    now = datetime.now()
    outdata = f'{now.strftime("%m/%d/%Y, %H:%M:%S")} heartbeat'
    logging.info(f'send: {outdata}')
    tcpserver.send(outdata.encode())
    indata = tcpserver.recv(1024)
    if len(indata) == 0:  # connect colosed
        tcpserver.close()
        logging.info(f'server closed connection.')
    logging.info(f'recv : {indata.decode()}')
    sleep(1)
