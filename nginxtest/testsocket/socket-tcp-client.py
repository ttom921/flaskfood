# socket-tcp-client.py
import socket

HOST = "192.168.40.191"
PORT = 7000

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpserver.connect((HOST, PORT))

while True:
    outdata = input('Please input message: ')
    print(f'send {outdata}')
    tcpserver.send(outdata.encode())
    indata = tcpserver.recv(1024)
    if len(indata) == 0:  # connect colosed
        tcpserver.close()
        print('server closed connection.')
    print(f'recv: {indata.decode()}')
