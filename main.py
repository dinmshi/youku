from Nodes import nodes
from Collect import collect
from Sqlhelper import sqlhelper



targetUrl = 'http://list.youku.com/category/show/c_97_a_%E9%9F%A9%E5%9B%BD_s_1_d_1_p_1.html?spm=a2h1n.8251845.0.0'

allNodes = nodes.getNodes(targetUrl)
nums = allNodes.__len__()
# print("总共 : " + str(nums) + "个剧")
for nodeKey in allNodes.keys() :
    videoInfo = allNodes.get(nodeKey)
    sqlhelper.insertVideo(videoInfo)

    collects = collect.getCollects(nodeKey)
    for su in collects:
        sqlhelper.insertEpisode(su)




