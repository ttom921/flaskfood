SERVER_URL = 'http://192.168.40.190'
DEBUG = False
API_VERSION = 'v0.8'
SERVER_HAS_SSL = False

SQLALCHEMY_ECHO = True  # Release 拿掉
SQLALCHEMY_BINDS_COMPANY = "mysql+pymysql://hisharp:Hisharp6f@192.168.40.209:3307/"
SQLALCHEMY_BINDS_COMPANY_LOG = "mysql://hisharp:Hisharp6f@192.168.40.209:3307/"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 200
SQLALCHEMY_MAX_OVERFLOW = 300
# 防止MySQL has gone away 問題
SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True}

LIVE_URL = "rtmp://192.168.40.155:1935/"
HLS_URL = "http://192.168.40.155:8080/"

KAFKA_SERVERS_IN = ['192.168.40.155:9097', '192.168.40.155:9098', '192.168.40.155:9099']
KAFKA_SERVERS_OUT = ['192.168.40.155:9097', '192.168.40.155:9098', '192.168.40.155:9099']

# ==========================================
# === === === === FTP Server === === === ===
# ==========================================
FTP_PATH = "/data/upload"

DB_ENGINE_ECHO = False
