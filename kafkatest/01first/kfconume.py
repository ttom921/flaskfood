import config
from kafka import KafkaConsumer
import time

def start_consumer():
    try:
        consumer =KafkaConsumer(config.TOPIC,
                                bootstrap_servers=config.SERVER,
                                )
        for msg in consumer:
            print(msg)
            print(f"topic = {msg.topic}") # topic default is string
            print(f"partition = {msg.partition}")  
            print(f"offset = {msg.offset}")   
            print(f"value = {msg.value.decode('utf-8')}")
            print(f"timestamp = {msg.timestamp}")       

    except KeyboardInterrupt:
        consumer.close()
if __name__ == '__main__':
    start_consumer()


# def start_consumer():
#     try:
#         consumer = KafkaConsumer(config.TOPIC, 
#                                  bootstrap_servers=config.SERVER)
#         for msg in consumer:
#             print(msg)
#     except KeyboardInterrupt:
#         consumer.close()
#     # consumer = KafkaConsumer('my_favorite_topic2', bootstrap_servers=config.SERVER,api_version=(0, 10, 1))
#     # for msg in consumer:
#     #     print(msg)
#     #     print("topic = %s" % msg.topic) # topic default is string
#     #     print("partition = %d" % msg.offset)
#     #     print("value = %s" % msg.value.decode()) # bytes to string
#     #     print("timestamp = %d" % msg.timestamp)
#     #     print("time = ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime( msg.timestamp/1000 )) )
   
# if __name__ == '__main__':
#     start_consumer()