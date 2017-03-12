import requests
import re
import random
import time
from proxy import proxy


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
            response = requests.get(url, headers=headers, proxies=self.getProxy(True))
            if response.status_code != 200:
                print("response.status_code : " + response.status_code)
                self.get(url, timeout, proxy, 6)
            if response.text == None:
                print("response.text == None")
                self.get(url, timeout, proxy().getProxy(), 6)
            print(response)
            return response
        except Exception as e:
            print(Exception)
            print(e)
            time.sleep(5)
            self.get(url, timeout, proxy().getProxy(), num_retries - 1)

    def getProxy(self, cache):
        if cache:
            return self.proxy
        else:
            self.proxy = proxy.getProxy()
            return self.proxy

request = DownLoad()
