import requests
import random
import json

class Proxy:
    ipList = []
    ipPortList = {}
    def __init__(self):
        self.ipList = []  ##初始化一个list用来存放我们获取到的IP
        self.ipPortList = {}  ##初始化一个list用来存放我们获取到的IPport
        ipListJson = requests.get("http://127.0.0.1:8000/")  ##不解释咯
        ipList = json.loads(ipListJson.text)
        for ip in ipList:
            self.ipList.append(ip[0])
            self.ipPortList[ip[0]] = ip[1]

    def getProxy(self):
        ip = str(random.choice(self.ipList))
        port = self.ipPortList.get(ip)
        proxies={
            'http':'http://%s:%s'%(ip,port),
            'https':'http://%s:%s'%(ip,port)
        }
        print(proxies)
        return proxies

proxy = Proxy()