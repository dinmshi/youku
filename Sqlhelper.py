from sqlalchemy import Column, Integer, String, DateTime, Numeric, create_engine, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BaseModel = declarative_base()

class VideoData(BaseModel):
    __tablename__ = 'y_video'
    id = Column(VARCHAR(255), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)
    img_url = Column(VARCHAR(255), nullable=False)
    types = Column(VARCHAR(255), nullable=False)



class EpisodeData(BaseModel):
    __tablename__ = 'y_episode'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False)
    video_url = Column(VARCHAR(255), nullable=False)
    video_id = Column(VARCHAR(255), nullable=False)


class SqlHelper():

    videoParams = {'title': VideoData.title, 'img_url': VideoData.img_url, 'types': VideoData.types}
    episodeParams = {'number': EpisodeData.number, 'video_url': EpisodeData.video_url, 'video_id': EpisodeData.video_id}

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:dswwjm2017@123.206.46.192/video_url?charset=utf8', echo=False)
        DB_Session = sessionmaker(bind=self.engine)
        self.session = DB_Session()


    def init_db(self):
        BaseModel.metadata.create_all(self.engine)


    def drop_db(self):
        BaseModel.metadata.drop_all(self.engine)


    def insertVideo(self, value):
        proxy = VideoData(id=value['id'], title=value['title'], img_url=value['img_url'], types=value['types'])
        self.session.add(proxy)
        self.session.commit()

    def insertEpisode(self, value):
        proxy = EpisodeData(number=value['number'], video_url=value['video_url'], video_id=value['video_id'])
        self.session.add(proxy)
        self.session.commit()
    #
    # def delete(self, conditions=None):
    #     if conditions:
    #         conditon_list = []
    #         for key in list(conditions.keys()):
    #             if self.params.get(key, None):
    #                 conditon_list.append(self.params.get(key) == conditions.get(key))
    #         conditions = conditon_list
    #         query = self.session.query(Proxy)
    #         for condition in conditions:
    #             query = query.filter(condition)
    #         deleteNum = query.delete()
    #         self.session.commit()
    #     else:
    #         deleteNum = 0
    #     return ('deleteNum', deleteNum)

    #
    # def update(self, conditions=None, value=None):
    #     '''
    #     conditions的格式是个字典。类似self.params
    #     :param conditions:
    #     :param value:也是个字典：{'ip':192.168.0.1}
    #     :return:
    #     '''
    #     if conditions and value:
    #         conditon_list = []
    #         for key in list(conditions.keys()):
    #             if self.params.get(key, None):
    #                 conditon_list.append(self.params.get(key) == conditions.get(key))
    #         conditions = conditon_list
    #         query = self.session.query(Proxy)
    #         for condition in conditions:
    #             query = query.filter(condition)
    #         updatevalue = {}
    #         for key in list(value.keys()):
    #             if self.params.get(key, None):
    #                 updatevalue[self.params.get(key, None)] = value.get(key)
    #         updateNum = query.update(updatevalue)
    #         self.session.commit()
    #     else:
    #         updateNum = 0
    #     return {'updateNum': updateNum}
    #
    #
    # def select(self, count=None, conditions=None):
    #     '''
    #     conditions的格式是个字典。类似self.params
    #     :param count:
    #     :param conditions:
    #     :return:
    #     '''
    #     if conditions:
    #         conditon_list = []
    #         for key in list(conditions.keys()):
    #             if self.params.get(key, None):
    #                 conditon_list.append(self.params.get(key) == conditions.get(key))
    #         conditions = conditon_list
    #     else:
    #         conditions = []
    #
    #     query = self.session.query(Proxy.ip, Proxy.port, Proxy.score)
    #     if len(conditions) > 0 and count:
    #         for condition in conditions:
    #             query = query.filter(condition)
    #         return query.order_by(Proxy.score.desc(), Proxy.speed).limit(count).all()
    #     elif count:
    #         return query.order_by(Proxy.score.desc(), Proxy.speed).limit(count).all()
    #     elif len(conditions) > 0:
    #         for condition in conditions:
    #             query = query.filter(condition)
    #         return query.order_by(Proxy.score.desc(), Proxy.speed).all()
    #     else:
    #         return query.order_by(Proxy.score.desc(), Proxy.speed).all()


    def close(self):
        pass


sqlhelper = SqlHelper()
sqlhelper.init_db()