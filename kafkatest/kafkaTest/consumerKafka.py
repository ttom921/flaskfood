from kafka import KafkaConsumer
import sys

# bootstrap_servers = ['192.168.46.204:9092', '192.168.46.225:9092', '192.168.40.209:9092']
bootstrap_servers = ['3.113.200.169:9091', '3.113.200.169:9092', '3.113.200.169:9093']
topicName = 'Control'

# consumer = KafkaConsumer (topicName, group_id = 'group1', bootstrap_servers = bootstrap_servers, auto_offset_reset = 'earliest')
consumer = KafkaConsumer (topicName, bootstrap_servers = bootstrap_servers, auto_offset_reset = 'earliest')

for msg in consumer:
    print(msg)
