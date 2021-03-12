from flask import Blueprint,request,make_response,jsonify

from libs.response import *
from libs.headers import *
from libs.utility import *
import json
from kafka.errors import KafkaError
from kafka.admin import KafkaAdminClient, NewTopic

# import sys


LOG_LEVEL_INFO()
# LOG_LEVEL_ERROR()
# sys.path.append("../..")

#example = Blueprint('index_page',__name__)
kafka = Blueprint(name="kafka", import_name=__name__)


@kafka.route("/index",methods=["GET"],endpoint = '_index')
def _index():
    return "kafka index"

@kafka.route("/topic",methods=["POST","DELETE"], endpoint = '_topic')
@flask_request_initial
def _topic(reqArgs):
    postData = json.loads(reqArgs.postData)
    logging.info(f"postData={postData}")
    
    if request.method == 'POST':
        topic= postData['topic']
        if topic == None:
            return "topic is none",RespCode.ARGS_ERROR
        return __createTopic(topic)   

    elif request.method == "DELETE":   
        topic= postData['topic']
        logging.info(f"DELETE postData={postData}")
        if topic == None:
            return "topic is none",RespCode.ARGS_ERROR
        return __delTopic(topic)     
    return ""
def __createTopic(topic):
    try:
        admin_client = KafkaAdminClient(
                bootstrap_servers=current_app.config["KFKA_URL"], 
                )
        #logging.info(f"admin_client={admin_client}")
        if admin_client == None:
            return "admin_client is none",RespCode.ARGS_ERROR   
        topic_list = []
        topic_list.append(NewTopic(name=topic, num_partitions=1, replication_factor=3))    
        
        res=admin_client.create_topics(new_topics=topic_list, validate_only=False)
        #logging.info(f"NewTopic res={res}")
        return ""
    except KafkaError as ke:
        # logging.info(f"except ={dir(ke)}")
        # logging.info(f"except ={ke}")
        # logging.info(f"except ke.errno={ke.errno}")
        # logging.info(f"except ke.message={ke.message}")
        return f"{ke.errno}-{ke.message}",RespCode.ARGS_ERROR 
    except Exception as e: 
        return  "exception ",RespCode.ARGS_ERROR  

def __delTopic(topic):
    try:
        admin_client = KafkaAdminClient(
                bootstrap_servers=current_app.config["KFKA_URL"], 
                )
        #logging.info(f"admin_client={admin_client}")
        if admin_client == None:
            return "admin_client is none",RespCode.ARGS_ERROR  
        topic_list = []
        topic_list.append(topic)    
        
        res=admin_client.delete_topics(topic_list)    
        #logging.info(f"NewTopic res={res}")
        return ""    
    except KafkaError as ke: 
         # logging.info(f"except ={dir(ke)}")
        # logging.info(f"except ={ke}")
        # logging.info(f"except ke.errno={ke.errno}")
        # logging.info(f"except ke.message={ke.message}")
        return f"{ke.errno}-{ke.message}",RespCode.ARGS_ERROR           
    except Exception as e: 
        logging.info(f"exception ={e}")
        #logging.info(f"exception ={dir(e)}")
        return  "exception ",RespCode.ARGS_ERROR  