SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'

GOPS_PATH = '/media/vdisk/gops'
IMAGES_PATH = '/media/vdisk/images'
FW_PATH = '/media/vdisk/fws'

GOPS_URL = '/event/gops'
IMAGES_URL = '/event/images'
FW_URL = '/fws'

CARID_IMG_PATH = '/usr/share/nginx/html/images/carids/'
QRCODE_PATH = '/usr/share/nginx/html/qrcode/'

GOP_DOWNLOAD_TIME = 3600    #GOP連結可以下載的有效時間
TOKEN_DURATION = 36000       #token 有效時間長度(s)
LP_WAITING_TIME = 5         #Long Polling時的總時間時間Sec 某些API不會使用這時間
LP_QUERY_SQL_TIME = 3       #Long Polling時Query DB的間隔時間Sec
LP_MAX_TIME = 1200          #Long Polling hold住連線最長時間 (不可大於Nginx的timeout時間)  目前沒用到項

GOP_DOWNLOAD_KEY = '4dL8zaNyD8FdITaS'
QRCODE_KEY = b'GEMN7HHCMCOjNpsn'
TOKEN_KEY = 'Xd03KgyZaZ0TbC82'
