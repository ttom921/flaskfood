from elasticsearch import Elasticsearch
import logging
import json

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
                    # datefmt='%m-%d %H:%M',
                    )
# logging.info(f"info")
# logging.debug(f"debug")


def create_index(es, indexname):
    logging.info(f"create_index")
    body = dict()
    body['settings'] = get_setting()
    body['mappings'] = get_mapping()
    logging.info(f"{json.dumps(body)}")  # 可以用json.dumps輸出來看格式有沒有包錯
    es.indices.create(index=indexname, body=body)


def get_setting():
    settings = {
        "index": {
            "number_of_shards": 3,
            "number_of_replicas": 2
        }
    }
    return settings


def get_mapping():
    mapppings = {
        "properties": {
            "date": {
                "type": "date"
            },
            "hdate": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss"
            },
            "car_uid": {
                "type": "keyword"
            },
            "event_name": {
                "type": "text"
            },
            "interval": {
                "type": "text"
            },
            "desc": {
                "type": "text"
            }
        }
    }
    return mapppings


def del_index(es, index_name):
    es.indices.delete(index=index_name, ignore=[400, 404])


if __name__ == "__main__":
    # 打上連接es的host和port
    es = Elasticsearch(hosts="192.168.83.129", port=9200)
    index_name = "es_event"
    # 創建
    create_index(es, index_name)
    #del_index(es, index_name)
