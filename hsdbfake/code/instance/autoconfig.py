import os
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))

# from instance.aws import *
# AUTO_CONFIG_FILE = 'aws.py'

from instance.hisharp import *
AUTO_CONFIG_FILE = 'hisharp.py'

# ======== Server Config ===========

server_config = {}
server_config["server_id"] = "d7b4d88a80b9f143bc36c6d7d562c369"
server_config["server_type"] = "all"
server_config["SQLALCHEMY_BINDS_COMPANY"] = SQLALCHEMY_BINDS_COMPANY
server_config["SQLALCHEMY_BINDS_COMPANY_LOG"] = SQLALCHEMY_BINDS_COMPANY_LOG
server_config["IMAGES_PATH"] = "/media/vdisk/images"
server_config["EVENT_VIDEO_PATH"] = "/media/vdisk/events"
server_config["EVENT_GOPS_PATH"] = "/higops/events"
server_config["EVENTS_URL"] = "/events"
server_config["SCHEDULE_ECHO"] = False
