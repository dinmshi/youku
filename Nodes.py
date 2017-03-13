import string

from bs4 import BeautifulSoup
from download import request
from Sqlhelper import VideoData

class Nodes:

    nodes = []

    def __init__(self):
        self.nodes = []

    def getNodes(self, startUrl):
        if startUrl == "" :
            return None

        startHtml = request.get(startUrl, 3)
        solp = BeautifulSoup(startHtml.text, 'lxml')

        attrs = {"class": "yk-col4 mr1"}
        lis = solp.find_all("li", attrs)
        p = {}
        httpStr = "http:"
        for li in lis:
            url = li.div.div.a["href"]
            if (url.find(httpStr) == -1):
                url = httpStr + url
            title = li.div.div.a["title"]
            img = li.div.div.img["src"]
            print("getNodes")
            p[url] = VideoData(id=url, title=title, img_url=img, types='types')

        nextPageLi = solp.find("li", class_="next")

        if nextPageLi.a != None:
            nextPageUrl = httpStr + nextPageLi.a["href"]

            print("get nextPageUrl")
            p1 = self.getNodes(nextPageUrl)
            print("update p")
            p.update(p1)
            return p
        else:
            print("return p")
            return p


        return p

nodes = Nodes()