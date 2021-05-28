from elasticsearch import Elasticsearch
import logging
import json

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
                    # datefmt='%m-%d %H:%M',
                    )
# logging.info(f"info")
# logging.debug(f"debug")


def del_index(es, index_name):
    es.indices.delete(index=index_name, ignore=[400, 404])


if __name__ == "__main__":
    # 打上連接es的host和port
    es = Elasticsearch(hosts="192.168.83.129", port=9200)
    index_name = "es_event"
    # 創建
    #create_index(es, index_name)
    del_index(es, index_name)
