"""duckdns.py

Script to update DNS from DuckDNS.org
"""

import configparser
import logging
import logging.handlers
import ssl
import urllib.parse
import urllib.request


logging.basicConfig(format=('%(asctime)s,%(msecs)d %(name)s %(levelname)s '
                    '%(message)s'), datefmt='%Y%m%d %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger('duckdns.py')
handler = logging.handlers.SysLogHandler()
logger.addHandler(handler)

config = configparser.ConfigParser()
config.read('config.ini')

domain = config['DUCKDNS']['domain']
token = config['DUCKDNS']['token']

payload = urllib.parse.urlencode({'domains': domain, 'token': token})
url = 'https://www.duckdns.org/update?{}'.format(payload)

context = ssl._create_unverified_context()
with urllib.request.urlopen(url, context=context) as response:
    data = response.read().decode()

logger.info(data)
