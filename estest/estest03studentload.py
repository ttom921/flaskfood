from elasticsearch import Elasticsearch
import logging
import json


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
                    # datefmt='%m-%d %H:%M',
                    )
# logging.info(f"info")
# logging.debug(f"debug")


def load_datas():
    datas = list()
    with open("student.csv", "r") as f:
        for data in f.readlines():
            sid, name, age, class_ = data.replace("\n", "").split(',')
            datas.append(
                {
                    "sid": sid,
                    "name": name,
                    "age": int(age),
                    "class": class_
                }
            )
    return datas


def create_data(es, datas):
    for data in datas:
        es.index(index="school", body=data)
        #es.index(index="school_members", body=data)


if __name__ == "__main__":
    # 打上連接es的host和port
    es = Elasticsearch(hosts="192.168.83.129", port=9200)
    datas = load_datas()
    create_data(es, datas)
