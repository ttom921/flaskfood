
from flask import Blueprint, request, current_app, jsonify, g
import sys
from database import *

from libs.utility.logs import *
LOG_LEVEL_INFO()
# sys.path.append("../..")


def flask_request_initial(func):
    def inner():
        reqArgs = RequestArgs(request)
        # # 驗證是否OK
        # if reqArgs.token_isok is False:
        #     return "", reqArgs.token
        # 取得ttomdb_session
        status, g.ttomdb_session = db.get_session("ttomdb")
        logging.info(f"status g.ttomdb_session={g.ttomdb_session}")
        return func(reqArgs)
    return inner


class RequestArgs(object):
    waiting = False
    token = None
    dvr_token = None
    token_isok = False
    userids = None
    userid = None
    groupids = None
    groupid = None
    dvrmodelid = None
    carids = None
    carid = None
    car_uid = None

    dvrids = None
    dvrid = None
    dvreid = None
    companyids = None
    companyid = None
    eventids = None
    eventid = None
    eventtypeid = None
    filepath = ""
    filename = ""
    # from       = None
    to = None
    limit = None
    offset = None
    postData = None
    serverid = None
    version = None
    config = None
    uploadToken = None
    uploadToken_isok = False
    status = None
    event_type_id = None
    event_type = None
    event_lock = None
    receiver = None
    send = None
    order = 'desc'
    gop_filter = False
    fw_id = None
    established = None
    bind = False
    level = None
    start_time = None
    end_time = None
    year = None
    month = None

    def __init__(self, request):
        #
        self.waiting = request.headers.get('Waiting') == "True"

        #
        self.auth = request.headers.get('Authorization')
        if self.auth == None:
            self.auth = request.args.get('Token')
        # self.token_isok, self.token = token_verified(
        #     current_app.config['TOKEN_KEY'], self.auth)

        self.dvr_token = request.headers.get('dvr_token')

        # List
        self.userids = request.args.getlist('userid')

        #
        self.userid = request.args.get('userid')

        # List
        self.groupids = request.args.getlist('groupid')

        self.dvrmodelid = request.args.get('dvrmodelid')

        #
        self.groupid = request.args.get('groupid')

        # List
        self.cmd_ids = request.args.getlist('cmd_id')

        #
        self.cmd_id = request.args.get('cmd_id')
        if self.cmd_id == None:
            self.cmd_id = request.form.get('cmd_id')

        # List
        self.carids = request.args.getlist('carid')

        #
        self.carid = request.args.get('carid')
        if self.carid == None:
            self.carid = request.form.get('carid')

        self.car_uid = request.args.get('car_uid')
        if self.car_uid == None:
            self.car_uid = request.form.get('car_uid')

        # List
        self.dvrids = request.args.getlist('dvrid')

        #
        self.dvrid = request.args.get('dvrid')

        #
        self.dvreid = request.args.get('dvr_eid')

        # List
        self.companyids = request.args.getlist('companyid')

        #
        self.companyid = request.args.get('companyid')

        # List
        self.eventids = request.args.getlist('eventid')

        #
        self.eventid = request.args.get('eventid')
        #
        self.eventtypeid = request.args.get('eventtypeid')
        #
        self.event_type = request.args.get('event_type')
        #
        self.event_lock = request.args.get('event_lock')
        #
        self.filepath = request.form.get('file_path')

        #
        self.filename = request.form.get('file_name')

        #
        #self.form = request.args.get('from')
        self.to = request.args.get('to')

        #
        self.limit = request.args.get('limit')
        self.offset = request.args.get('offset')

        #
        self.postData = request.data
        # list
        self.serverid = request.args.getlist('serverid')

        #
        self.version = request.args.get('version')

        #
        self.config = request.form.get('config')

        #
        self.status = request.args.get('status')

        #
        upload_auth = request.headers.get('Token')
        # self.uploadToken_isok, self.uploadToken = token_verified(
        #     current_app.config['TOKEN_KEY'], upload_auth)

        #
        self.event_type_id = request.args.get('event_type_id')
        #
        self.receiver = request.args.get('receiver')
        #
        self.send = request.args.get('send')
        #
        self.order = request.args.get('order')
        #
        self.gop_filter = request.args.get('gop_filter')
        #
        self.fw_id = request.args.get('fw_id')

        self.established = request.args.get('established')
        self.bind = request.args.get('bind')

        self.level = request.args.get('level')

        self.start_time = request.args.get('start_time')
        self.end_time = request.args.get('end_time')
        # 年 和月份
        self.year = request.args.get('year')
        self.month = request.args.get('month')
