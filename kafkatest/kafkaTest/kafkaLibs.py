from kafka import KafkaProducer


# === === === === === === === === === === === === === === === === === === === === === === === ===
bootstrap_servers = ['192.168.46.204:9092', '192.168.46.225:9092', '192.168.40.209:9092']

def kafka_init():
    global producer
    producer = KafkaProducer(bootstrap_servers = bootstrap_servers, api_version = (0, 10))

def kafka_produce(topicName, bytesMsg):
    future = producer.send(topicName, bytesMsg)
    # future = producer.send('my_topic' , key= b'my_key', value= b'my_value', partition= 0)
    
    result = future.get(timeout= 10)
    print(result)
