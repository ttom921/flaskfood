
SERVER_PORT = 5000
DEBUG = False
SQLALCHEMY_ECHO = False
API_VERSION = 'v0.0'

AUTH_TOKEN_NAME="authtoken"
# 過濾url
IGNORE_URLS=[
    "^/{0}/user/login".format(API_VERSION),
    "/"
]
IGNORE_CHECK_LOGIN_URLS=[
    "^/favicon.ico",
]
# 過濾url
