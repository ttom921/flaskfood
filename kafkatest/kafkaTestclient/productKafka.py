from kafka import KafkaProducer
from time import sleep


def start_producer():
    # bootstrap_servers = ['192.168.46.204:9092', '192.168.46.225:9092', '192.168.40.209:9092']
    bootstrap_servers = ['3.113.200.169:9091', '3.113.200.169:9092', '3.113.200.169:9093']
    topicName = 'Control'

    producer = KafkaProducer(bootstrap_servers=bootstrap_servers, api_version=(0, 10))
    for i in range(0, 100000):
        msg = 'msg is ' + str(i)
        future = producer.send(topicName, msg.encode('utf-8'))
        # future = producer.send('my_topic' , key= b'my_key', value= b'my_value', partition= 0)

        result = future.get(timeout=30)
        print(result)

        sleep(3)


if __name__ == '__main__':
    start_producer()
