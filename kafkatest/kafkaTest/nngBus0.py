from pynng import Bus0, Timeout

address = 'tcp://127.0.0.1:12343'

import time

"""
python3 nngBus0.py node1 'ipc:///tmp/control.ipc'
python3 nngBus0.py node2 'ipc:///tmp/control.ipc'
python3 nngBus0.py node3 'ipc:///tmp/control.ipc'
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

def node2(name, url):
    iCnt = 0
    with Bus0(dial=url, recv_timeout=100) as s1:
        while True:
            
            try:
                s1.send(name)
                time.sleep(1)
                msg = s1.recv()
                print(f'[{name}] received {msg}')
                # assert False, "this is never reached"
            except Timeout:
                print('s2 is not connected directly to s0!')
        

if __name__ == '__main__':
    import sys
    assert len(sys.argv) == 3
    if sys.argv[1] == 'node1':
        node1(sys.argv[2])
    elif sys.argv[1] == 'node2':
        node2(b'Node2', sys.argv[2])
    elif sys.argv[1] == 'node3':
        node2(b'Node3', sys.argv[2])
    else:
        print('''Usage:
        python pair.py node1 <url>
        python pair.py node1 <url>''')
