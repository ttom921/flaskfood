from elasticsearch import Elasticsearch
import logging
import json


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
                    # datefmt='%m-%d %H:%M',
                    )
# logging.info(f"info")
# logging.debug(f"debug")


def get_query():
    query = {
        "query": {
            "bool": {
                "must": {
                    "term": {
                        "age": 20
                    }
                }
            }
        }
    }
    return query


if __name__ == "__main__":
    # 打上連接es的host和port
    es = Elasticsearch(hosts="192.168.83.129", port=9200)
    query = get_query()
    #result = es.search(index="school", body=query)
    result = es.search(index="school_members", body=query)
    logging.info(json.dumps(result, ensure_ascii=False))
