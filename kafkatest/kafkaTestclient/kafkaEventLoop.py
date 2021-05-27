import asyncio

import time
from time import sleep

from pynng import Bus0, Timeout

from kafkaLibs import kafka_init, kafka_produce
from kafkaControl import kafka_ControlProcess

control_url = "ipc:///tmp/control.ipc"

# === === === === === === === === === === === === === === === === === === === === === === === ===
async def firstWorker():
    while True:
        await asyncio.sleep(1)
        print("First Worker Executed")

async def secondWorker():
    while True:
        await asyncio.sleep(1)
        print("Second Worker Executed")

if __name__ == '__main__':
    kafka_init()
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(kafka_ControlProcess())
        # asyncio.ensure_future(firstWorker())
        # asyncio.ensure_future(secondWorker())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
