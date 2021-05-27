from elasticsearch import Elasticsearch
import logging
import json


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
                    # datefmt='%m-%d %H:%M',
                    )
# logging.info(f"info")
# logging.debug(f"debug")


def create_index(es):
    logging.info(f"create_index")
    body = dict()
    body['settings'] = get_setting()
    body['mappings'] = get_mapping()
    logging.info(f"{json.dumps(body)}")  # 可以用json.dumps輸出來看格式有沒有包錯
    es.indices.create(index="school_members", body=body)


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
            "sid": {
                "type": "text"
            },
            "name": {
                "type": "text"
            },
            "age": {
                "type": "integer"
            },
            "class": {
                "type": "keyword"
            }
        }
    }
    return mapppings


def get_indexinfo(es):
    # index 指定要get哪個index的資訊
    result = es.indices.get(index="school_members")
    logging.info(result)


def exists(es):
    result = es.indices.exists(index="school_members")
    logging.info(result)


if __name__ == "__main__":
    # 打上連接es的host和port
    es = Elasticsearch(hosts="192.168.83.129", port=9200)
    # 創建
    create_index(es)
    # get :回傳index信息
    # get_indexinfo(es)
    # exists:查看index是否存在，回傳True/False
    # exists(es)
