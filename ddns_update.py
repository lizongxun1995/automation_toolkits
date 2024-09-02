import time
from os import times

import requests
from loguru import logger


class DDNSClient:
    url = 'https://dynv6.com/api/update?'
    ipv4_query_address = 'https://4.ipw.cn/'
    ipv6_query_address = 'https://6.ipw.cn/'
    params = {
        'zone': '', # 域名
        'token': '', # token
        'ipv4': '',
        'ipv6': ''
    }

    def __init__(self,sleep_time=60):
        while True:
            logger.info('开始更新')
            self.update_params()
            result = requests.get(self.url,self.params).text
            logger.info(result)
            logger.info(f'sleep {sleep_time}s')
            time.sleep(sleep_time)

    def update_params(self):
        try:
            ipv4 = requests.get(self.ipv4_query_address).text
            ipv6 = requests.get(self.ipv6_query_address).text
            self.params['ipv4'] = ipv4
            self.params['ipv6'] = ipv6
            logger.info(ipv4)
            logger.info(ipv6)
        except:
            ...


if __name__ == '__main__':
    DDNSClient(300)
