"""duckdns.py
Script to update DNS from DuckDNS.org
"""

import requests
import logging
import logging.handlers
import configparser


logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y%m%d %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger('duckdns.py')
handler = logging.handlers.SysLogHandler()
logger.addHandler(handler)

config = configparser.ConfigParser()
config.read('config.ini')

domain = config['DUCKDNS']['domain']
token = config['DUCKDNS']['token']

url = 'https://www.duckdns.org/update'
payload = {'domains': domain, 'token': token}
update = requests.get(url, params=payload)

logger.info(update.text)
