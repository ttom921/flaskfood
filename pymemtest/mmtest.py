# post json
# import logging
# import requests
# import json
# from time import sleep
# # logging.basicConfig(level=logging.DEBUG)

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
#                     #datefmt='%m-%d %H:%M',
#                     )

# data = {
#     "level": 1,		# 1=> 設定公司, 2=> 設定車隊, 3=> 設定車輛
#     "group_id": 1,  # // level = 2 的時候才需要設定
#     "car_id": 1,  # // level = 3 的時候才需要設定
#     "data": "thissiatestjsonjsontokenthissiatestjsonjsontokenthissiatestjsonjsontokenthissiatestjsonjsontokenthissiatestjsonjsontokenthissiatestjsonjsontokenthissiatestjsonjsontoken",
# }
# # heasers中加上contect-type
# headers = {'Content-Type': 'application/json'}

# # post 時，將data字典形式的參數用json轉換成json格式
# url = "http://192.168.40.191/v0.0/events"
# while True:
#     response = requests.post(url=url, headers=headers)
#     # print(dir(response))
#     # print(f"response.status_code={response.status_code}")
#     logging.info(f"response.status_code={response.status_code}")
#     sleep(0.3)


import logging
import requests
import json
from time import sleep
# logging.basicConfig(level=logging.DEBUG)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(lineno)s] [PID %(process)d] %(levelname)-7s %(message)s ',
                    # datefmt='%m-%d %H:%M',
                    )

data = {
    "level": 1,		# 1=> 設定公司, 2=> 設定車隊, 3=> 設定車輛
    "group_id": 1,  # // level = 2 的時候才需要設定
    "car_id": 1,  # // level = 3 的時候才需要設定
    "data": "thissiatestjsonjsontokenthissiatestjsonjsontokenthissiatestjsonjsontokenthissiatestjsonjsontokenthissiatestjsonjsontokenthissiatestjsonjsontokenthissiatestjsonjsontoken",
}
# heasers中加上contect-type
headers = {'Content-Type': 'application/json'}
serverip = "192.168.40.191:5000"
#serverip = "192.168.40.191"
# post 時，將data字典形式的參數用json轉換成json格式
url = f"http://{serverip}/v0.0/events"

# while True:
#     response = requests.post(url=url, headers=headers)
#     # print(dir(response))
#     # print(f"response.status_code={response.status_code}")
#     logging.info(f"response.status_code={response.status_code}")
#     sleep(0.3)


# Start some API Calls
for _ in range(10000):
    requests.post(url=url, headers=headers, data=data)
    sleep(0.1)

# Memory usage after
resp = requests.get(f'http://{serverip}/v0.0/showmm')
print(resp.text)
