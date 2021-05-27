from pynng import Bus0, Timeout

address = 'tcp://127.0.0.1:12343'

import time

"""
python3 kafkaSend.py node1 'ipc:///tmp/control.ipc'
python3 kafkaSend.py message 'ipc:///tmp/control.ipc'
"""

def node1(url):
    with Bus0(listen=url, recv_timeout=100) as s0:
        name = b'Node1'
        while True:
            
            try:
                msg = s0.recv_msg()
                print(f'[{name}] received {msg.bytes}')
                time.sleep(1)
                print(f'[{name}] send {name}')
                s0.send(name)
                # assert False, "this is never reached"
            except Timeout:
                print('s0 is not connected directly to s1!')

def node2(messageStr, url):
    iRetry = 3
    with Bus0(dial=url, recv_timeout=100) as s1:
        while True:
            
            try:
                iRetry = iRetry - 1
                if iRetry < 0:
                    print(f"iRetry = {iRetry}")
                    break
                
                s1.send(messageStr.encode("UTF-8"))
                #time.sleep(1)
                msg = s1.recv()
                print(f'[node2] received {messageStr}')
                break
                # assert False, "this is never reached"
            except Timeout:
                print('s2 is not connected directly to s0!')
        

if __name__ == '__main__':
    import sys
    assert len(sys.argv) == 3
    if sys.argv[1] == 'node1':
        node1(sys.argv[2])
    else:
        node2(sys.argv[1], sys.argv[2])
