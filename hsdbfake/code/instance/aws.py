SERVER_URL = 'http://www.nvtfms.com'
DEBUG = False
API_VERSION = 'v0.5'
SERVER_HAS_SSL = False

SQLALCHEMY_ECHO = False  # Release 拿掉
SQLALCHEMY_BINDS_COMPANY = "mysql://hisharp:Hisharp6f@172.30.20.5:3306/"
SQLALCHEMY_BINDS_COMPANY_LOG = "mysql://hisharp:Hisharp6f@172.30.20.5:3306/"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 200
SQLALCHEMY_MAX_OVERFLOW = 300
# 防止MySQL has gone away 問題
SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True}

LIVE_URL = "rtmp://www.nvtfms.com:1935/"
HLS_URL = "http://www.nvtfms.com:8080/"

KAFKA_SERVERS_IN = ['172.30.50.50:9097', '172.30.50.50:9098', '172.30.50.50:9099']
KAFKA_SERVERS_OUT = ['www.nvtfms.com:9097', 'www.nvtfms.com:9098', 'www.nvtfms.com:9099']

# ==========================================
# === === === === FTP Server === === === ===
# ==========================================
FTP_PATH = "/data/upload"

DB_ENGINE_ECHO = False
