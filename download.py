import requests
import re
import random
import time
from proxy import proxyX


class DownLoad:
    user_agent_list = []
    proxy = None

    def __init__(self):
        # 导入数据集并随机获取一个User-Agent
        f = open('user_agent', 'r')
        for date_line in f:
            self.user_agent_list.append(date_line.replace('\r\n', ''))

    def get(self, url, timeout, num_retries=6):
        userAgent = random.choice(self.user_agent_list).rstrip()
        print(userAgent)
        headers = {
            "User-Agent": userAgent,
        }

        try:
            response = requests.get(url, headers=headers, proxies=self.getProxy())
            if response.status_code != 200:
                print("response.status_code : " + response.status_code)
                self.get(url, timeout, self.getProxy())
            if response.text == None:
                print("response.text == None")
                self.get(url, timeout, self.getProxy())
            print(response)
            return response
        except Exception as e:
            print(Exception)
            print(e)
            time.sleep(5)
            self.get(url, timeout, self.getProxy())

    def getProxy(self):
        if self.proxy == None:
            self.proxy = proxyX

        print(self.proxy)
        return self.proxy

request = DownLoad()
