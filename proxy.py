import requests
import random
import json

class Proxy:
    ipList = []
    ipPortList = {}
    def __init__(self):
        self.ipList = []
        self.ipPortList = {}
        ipListJson = requests.get("http://127.0.0.1:8000/")
        print(ipListJson)
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