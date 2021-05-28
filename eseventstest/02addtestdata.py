from elasticsearch import Elasticsearch
import logging
import json
from psutil._compat import xrange
import random

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
                    # datefmt='%m-%d %H:%M',
                    )
# logging.info(f"info")
# logging.debug(f"debug")

# "date": {
#     "type": "date"
# },
#  "hdate": {
#                 "type": "date",
#                 "format": "yyyy-MM-dd HH:mm:ss"
#             },
# "car_uid": {
#     "type": "keyword"
# },
# "event_name": {
#     "type": "text"
# },
# "interval": {
#     "type": "text"
# },
# "desc": {
#     "type": "text"
# }


def __getEpochtimeDay(year, month, day):
    import datetime
    import calendar
    hour = random.randint(1, 23)
    min = random.randint(1, 59)
    sec = random.randint(1, 59)
    starttime = f"{year}-{month}-{day:02d} {hour}:{min}:{sec}"
    # logging.info(f"starttime={starttime}")

    #endtime=f"{year}-{month}-{day:02d} 23:59:59"
    # 取得GMT的時間
    startdt = datetime.datetime.strptime(f"{starttime}", "%Y-%m-%d %H:%M:%S")
    strtime = datetime.datetime.strftime(startdt, '%Y-%m-%d %H:%M:%S')
    logging.info(f"strtime={strtime}")
    #enddt=datetime.datetime.strptime(f"{endtime}", "%Y-%m-%d %H:%M:%S")
    startgmt = calendar.timegm(startdt.timetuple())
    # endgmt=calendar.timegm(enddt.timetuple())
    return startgmt, strtime


def genTestData(es):
    eventnamelst = [
        'Acceleration',
        'Deceleration',
        'Sharp_Turn',
        'LDWS',
        'OverSpeed',
        'OverEngine',
        'Panic',
        'Gsensor',
        'Vloss_1',
        'Vloss_2',
        'Vloss_3',
        'Vloss_4',
        'Vloss_5',
        'Vloss_6',
        'Vloss_7',
        'Vloss_8',
        'SSD_Error',
        'SD_Error',
        'System_Error',
        'ACC_ON',
        'ACC_OFF',
        'Alarm_1',
        'Alarm_2',
        'Alarm_3',
        'Alarm_4',
        'Alarm_5',
        'Alarm_6',
        'Alarm_7',
        'Alarm_8',
        'USER_DOWNLOAD',
    ]
    eventlen = len(eventnamelst) - 1
    carlen = 10
    index_name = "es_event"
    utctime, strtime = __getEpochtimeDay(2021, 5, 1)
    logging.info(f"utctime={utctime}")
    for i in xrange(0, 1):
        randev = random.randint(0, eventlen)
        randcar = random.randint(0, carlen)
        testdata = {
            "date": utctime,
            "hdate": strtime,
            "car_uid": f"car{randcar:06d}",
            "event_name": f"{eventnamelst[randev]}",
            "interval": "month",
            "desc": f"desc-{utctime}"
        }
        es.index(index=index_name, body=testdata)


if __name__ == "__main__":
    es = Elasticsearch(hosts="192.168.83.129", port=9200)
    genTestData(es)
