SERVER_URL = 'http://192.168.40.191'
DEBUG = False
API_VERSION = 'v0.6'
SERVER_HAS_SSL = False

SQLALCHEMY_ECHO = False # Release 拿掉
SQLALCHEMY_BINDS_COMPANY = "mysql://hisharp:Hisharp6f@192.168.40.209:3307/"
SQLALCHEMY_BINDS_COMPANY_LOG = "mysql://hisharp:Hisharp6f@192.168.40.209:3307/"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 200
SQLALCHEMY_MAX_OVERFLOW = 300
# 防止MySQL has gone away 問題
SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True}

REDIS_URL = 'redis://localhost'
LIVE_URL  = "rtmp://192.168.40.209:1935/"

DB_ENGINE_ECHO = False
