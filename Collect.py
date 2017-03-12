from bs4 import BeautifulSoup
from download import request
from Sqlhelper import EpisodeData

class Collect:

    def getCollects(self, nodsUrl):
        start_html = request.get(nodsUrl, 3)
        Soup = BeautifulSoup(start_html.text, 'lxml')
        herfs = Soup.find_all("a", "sn")
        p = {}
        httpStr = "http:"
        for a in herfs:
            url = a["href"]
            if (url.find(httpStr) == -1):
                url = httpStr + url
            suNum = a.span.string
            p[url] = EpisodeData(number=suNum, video_url=url, video_id=nodsUrl)
            print(a["href"])
            print(a.span)

        nums = p.__len__()
        print("总共 : " + str(nums) + "集")
        return p

collect = Collect()