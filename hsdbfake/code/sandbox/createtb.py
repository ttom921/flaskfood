# --------------路徑-------------------
import os
import sys
from os import path
# D: \Project\imooc\www\hsdbfake\code\run.py
sys.path.append(path.dirname(path.dirname((path.abspath(__file__)))))
# print(f"sys.path={sys.path}")
# --------------路徑-------------------
# 使用log
from libs.utility.logs import *

LOG_LEVEL_INFO()
# LOG_LEVEL_ERROR()
logging.info(f"create tb")
