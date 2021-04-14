from flask import Blueprint, request, make_response, jsonify, g, current_app

from libs.response import *
from libs.headers import *
from libs.utility import *
import json
import time
import datetime
from kafka.errors import KafkaError
from kafka.admin import KafkaAdminClient, NewTopic

from kafka import KafkaProducer

from multiprocessing import Value
# import sys

MsgCount = Value('i', 0)
LOG_LEVEL_INFO()
# LOG_LEVEL_ERROR()
# sys.path.append("../..")

# example = Blueprint('index_page',__name__)
kafka = Blueprint(name="kafka", import_name=__name__)


@kafka.route("/index", methods=["GET"], endpoint='_index')
def _index():
    return "kafka index"


# region 建立和刪除kafka的topic
"""
建立和刪除kfka的topic

http://{{ip}}/{{ver}}/kafka/topic
POST
{
    "topic" : "topic_name",
}
DELERE
{
    "topic" : "topic_name",
}
"""


@kafka.route("/topic", methods=["POST", "DELETE"], endpoint='_topic')
@flask_request_initial
def _topic(reqArgs):
    postData = json.loads(reqArgs.postData)
    logging.info(f"postData={postData}")

    if request.method == 'POST':
        topic = postData['topic']
        if topic == None:
            return "topic is none", RespCode.ARGS_ERROR
        return __createTopic(topic)

    elif request.method == "DELETE":
        topic = postData['topic']
        logging.info(f"DELETE postData={postData}")
        if topic == None:
            return "topic is none", RespCode.ARGS_ERROR
        return __delTopic(topic)
    return ""


def __createTopic(topic):
    try:
        admin_client = KafkaAdminClient(
            bootstrap_servers=current_app.config["KFKA_URL"],
        )
        # logging.info(f"admin_client={admin_client}")
        if admin_client == None:
            return "admin_client is none", RespCode.ARGS_ERROR
        topic_list = []
        topic_list.append(NewTopic(name=topic, num_partitions=3, replication_factor=2))

        res = admin_client.create_topics(new_topics=topic_list, validate_only=False)
        # logging.info(f"NewTopic res={res}")
        admin_client.close()
        return ""
    except KafkaError as ke:
        # logging.info(f"except ={dir(ke)}")
        # logging.info(f"except ={ke}")
        # logging.info(f"except ke.errno={ke.errno}")
        # logging.info(f"except ke.message={ke.message}")
        admin_client.close()
        return f"{ke.errno}-{ke.message}", RespCode.ARGS_ERROR

    except Exception as e:
        admin_client.close()
        return "exception ", RespCode.ARGS_ERROR


def __delTopic(topic):
    try:
        admin_client = KafkaAdminClient(
            bootstrap_servers=current_app.config["KFKA_URL"],
        )
        # logging.info(f"admin_client={admin_client}")
        if admin_client == None:
            return "admin_client is none", RespCode.ARGS_ERROR
        topic_list = []
        topic_list.append(topic)

        res = admin_client.delete_topics(topic_list)
        admin_client.close()
        # logging.info(f"NewTopic res={res}")
        with MsgCount.get_lock():
            MsgCount.value = 0
        return ""
    except KafkaError as ke:
        admin_client.close()
        # logging.info(f"except ={dir(ke)}")
        # logging.info(f"except ={ke}")
        # logging.info(f"except ke.errno={ke.errno}")
        # logging.info(f"except ke.message={ke.message}")
        return f"{ke.errno}-{ke.message}", RespCode.ARGS_ERROR
    except Exception as e:
        admin_client.close()
        logging.info(f"exception ={e}")
        # logging.info(f"exception ={dir(e)}")
        return "exception ", RespCode.ARGS_ERROR
# endregion 建立和刪除kafka的topic

# region 傳送kafka


@kafka.route("/send", methods=["POST", "DELETE"], endpoint='_send')
@flask_request_initial
def _send(reqArgs):
    logging.info(f"MsgCount.value ={MsgCount.value}")
    postData = json.loads(reqArgs.postData)
    logging.info(f"postData={postData}")
    if request.method == 'POST':
        __kafkaSend(postData)
    return ""


def __kafkaSend(postData):
    logging.info(f"current_app.config['KFKA_URL'] ={current_app.config['KFKA_URL']}")
    server_list = ["192.168.40.191:9092", "192.168.40.191:9093", "192.168.40.191:9094"]
    logging.info(f"server_list ={server_list}")
    # current_app.config["KFKA_URL"]
    producer = KafkaProducer(
        bootstrap_servers=current_app.config["KFKA_URL"],
        value_serializer=lambda m: json.dumps(m).encode()
    )
    try:

        topic = postData['topic']
        if topic == None:
            return "topic is none", RespCode.ARGS_ERROR

        #logging.info(f"MsgCount.value ={MsgCount.value}")
        send_data = {
            "num": MsgCount.value,
            "ts": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "data": postData['data']
        }
        logging.info(f"send_data ={send_data}")
        producer.send(topic, send_data)

        with MsgCount.get_lock():
            MsgCount.value += 1

        # producer.close()
        return ""
    except KafkaError as ke:
        # producer.close()
        return f"{ke.errno}-{ke.message}", RespCode.ARGS_ERROR
    except Exception as e:
        # producer.close()
        logging.info(f"exception ={e}")
        # logging.info(f"exception ={dir(e)}")
        return "exception ", RespCode.ARGS_ERROR
    finally:
        logging.info(f"finally-->producer.close()")
        producer.close()
# endergion 傳送kafka
