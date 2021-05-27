import asyncio
from aiokafka import AIOKafkaConsumer

bootstrap_servers = ['192.168.46.204:9092', '192.168.46.225:9092', '192.168.40.209:9092']
# bootstrap_servers = ['3.113.200.169:9091', '3.113.200.169:9092', '3.113.200.169:9093']
topicName = 'Control'

async def main(loop):
    ### 初始化消費者
    consumer = AIOKafkaConsumer(
        topicName,
        group_id='hs_server',
        loop=loop,
        auto_offset_reset = 'earliest',
        bootstrap_servers = bootstrap_servers,
        api_version="auto",
        metadata_max_age_ms=(30 * 1000),
    )
    ### 連接
    await consumer.start()
    ### 獲取消息
    data = await consumer.getmany()
    print(data)
    if data:
        for tp, message in data.items():
            print('tp>>>', tp)
            print(tp.topic)
            print('message>>', message)
            for msg in message:
                print(msg)
                print(msg.timestamp, msg.offset)
                v = msg.value
                print(v)
    ### 斷開
    await consumer.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
