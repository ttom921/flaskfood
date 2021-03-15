import json
import time
import datetime
import config
from kafka import KafkaProducer


def start_producer():
    producer = KafkaProducer(
        bootstrap_servers=config.SERVER,
        value_serializer=lambda m: json.dumps(m).encode()
    )
    for i in range(100):
        data = {
            "num": i,
            "ts": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        producer.send(config.TOPIC, data)
        print(f"send data={data}")
        time.sleep(1)
    producer.close()


if __name__ == "__main__":
    start_producer()

# producer = KafkaProducer(bootstrap_servers=config.SERVER,
#                          value_serializer=lambda m:json.dumps(m).encode(),
#                          api_version=(0, 10, 1))

# for i in range(100):
#     data ={'num':1,'ts':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
#     producer.send(config.TOPIC,data)
#     time.sleep(2)

# import config
# from kafka import KafkaProducer
# from time import sleep

# def start_producer():
#     # producer = KafkaProducer(bootstrap_servers=config.SERVER,api_version=(0, 10, 1))
#     # for i in range(0,5):
#     #     msg = 'msg is ' + str(i)
#     #     producer.send('my_favorite_topic2', msg.encode('utf-8'))
#     #     sleep(3)
#     #producer = KafkaProducer(bootstrap_servers="localhost:9092")
#     # producer = KafkaProducer(bootstrap_servers=config.SERVER)
#     # for i in range(10):
#     #     producer.send("test", "Hello {}".format(i).encode("utf-8"))
#     # producer.close()

# if __name__ == '__main__':
#     start_producer()
