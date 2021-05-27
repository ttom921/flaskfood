from pynng import Bus0, Timeout
from kafkaLibs import kafka_produce

control_url = "ipc:///tmp/control.ipc"

# === === === === === === === === === === === === === === === === === === === === === === === ===
async def kafka_ControlProcess():
    with Bus0(listen=control_url, recv_timeout=1000) as s0:
        name = b'Node1'
        while True:
            try:
                msg = await s0.arecv_msg()
                print(f'[{name}] received {msg.bytes}')
                # time.sleep(1)
                print(f'[{name}] send ACK')
                s0.send(b"ACK")   # ack
                # assert False, "this is never reached"
                kafka_produce("firstTopic", msg.bytes)
            except Timeout:
                #print('ControlTopic Timeout!')
                msg = ""
            except:
                print("[Error] Something went wrong")
                break
