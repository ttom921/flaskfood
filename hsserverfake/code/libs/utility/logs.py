import logging
import coloredlogs

coloredlogs.DEFAULT_FIELD_STYLES = {
            'hostname': {'color': 'magenta'},
            'programname': {'color': 'cyan'},
            'name': {'color': 'blue'},
            'levelname': {'color': 'white', 'bold': True},
            'asctime': {'color': 'magenta'}}

coloredlogs.DEFAULT_LEVEL_STYLES = {
                'info': {'color': 'green'},
                'notice': {'color': 'magenta'},
                'verbose': {'color': 'green'},
                'success': {'color': 'green', 'bold': True},
                'spam': {'color': 'cyan'},
                'critical': {'color': 'white', 'bold': True, 'background':'red'},
                'error': {'color': 'red'},
                'debug': { },
                'warning': {'color': 'yellow', 'bold': True}}    


def LOG_LEVEL_DEBUG():
    coloredlogs.install(level='DEBUG', fmt='%(asctime)s.%(msecs)03d [%(filename)s:%(lineno)s] %(levelname)-7s %(message)s ')

def LOG_LEVEL_INFO():
    coloredlogs.install(level='INFO', fmt='%(asctime)s.%(msecs)03d [%(filename)s:%(lineno)s] %(levelname)-7s %(message)s ')

def LOG_LEVEL_ERROR():
    coloredlogs.install(level='ERROR', fmt='%(asctime)s.%(msecs)03d [%(filename)s:%(lineno)s] %(levelname)-7s %(message)s ')

# logging 範例
def LOG_EXAMPLE():
    logging.debug('logging.debug: Hello debug!')
    logging.info('logging.info: Hello info!')
    logging.warning('logging.warning: Hello warning! debugFaile')
    logging.error('logging.error: Hello error!')
    logging.critical('logging.critical: Hello critical!')                


def START():
     logging.info(' ____ _____  _    ____ _____ ')
     logging.info('/ ___|_   _|/ \  |  _ \_   _|')
     logging.info('\___ \ | | / _ \ | |_) || |  ')
     logging.info(' ___) || |/ ___ \|  _ < | |  ')
     logging.info('|____/ |_/_/   \_\_| \_\|_|  ')
     logging.info('                             ')


def END():
    logging.info(' ___   _  _   ___   ')
    logging.info('| __| | \| | |   \  ')
    logging.info('| _|  | .` | | |) | ')
    logging.info('|___| |_|\_| |___/  ')
    logging.info('                    ')