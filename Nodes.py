import string

from bs4 import BeautifulSoup
from download import request
from Sqlhelper import VideoData
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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

            p[url] = VideoData(id=url, title=title, img_url=img, types='types')

        nextPageLi = solp.find("li", class_="next")

        b = nextPageLi.a != None

        if nextPageLi.a != None:
            nextPageUrl = httpStr + nextPageLi.a["href"]

            p1 = self.getNodes(nextPageUrl)

            p.update(p1)
            return p
        else:

            return p


        return p

nodes = Nodes()