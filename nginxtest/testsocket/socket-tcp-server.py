# socket-tcp-server.py
import socket

HOST = "127.0.0.1"
PORT = 7000

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpserver.bind((HOST, PORT))
tcpserver.listen(5)

print(f'server start at"{HOST}:{PORT}')
print(f'wait for connection ....')


while True:
    conn, addr = tcpserver.accept()
    print(f'connected by {addr}')

    while True:
        indata = conn.recv(1024)
        if len(indata) == 0:  # connect closed
            conn.close()
            print('client closed connection.')
            break
        print(f'recv: {indata.decode()}')

        outdata = f'echo {indata.decode()}'
        conn.send(outdata.encode())
