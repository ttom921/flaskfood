from websocket import create_connection

def client_handle():
    ws = create_connection('ws://192.168.83.128:8540/test')
    while True:
        if ws.connected:
            ws.send('hi,i am ws client')
            result = ws.recv()
            print(f"client received:{result}")
            # ws.close()

if __name__ == "__main__":
    client_handle()