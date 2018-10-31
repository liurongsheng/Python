import pymysql
import pymongo
from movieSite.items import MoviesiteItem

class MovieMySQLPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        db = pymysql.connect(
            host="127.0.0.1",
            user='root',
            password='admin123',
            database='pymysql',
            port=3306
        )
        cursor = db.cursor()
        sql = """
            insert into movie(
                movieTitle,movieImgUrl,movieStatus, pushTime,movieDetailUrl,movieDetailDirect, movieDetailActors,movieDetailType,movieDetailRelease,
                movieDetailCountry,movieDetailLanguage,movieDetailGrade, movieDetailStory
              ) 
              values(null,%s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s);
        """
        cursor.execute(sql,[item['movieTitle'],item['movieImgUrl'],item['movieStatus'], item['pushTime'],item['movieDetailUrl'],item['movieDetailDirect'],
                            item['movieDetailActors'],item['movieDetailType'],item['movieDetailRelease'], item['movieDetailCountry'],item['movieDetailLanguage'],
                            item['movieDetailGrade'], item['movieDetailStory'] ])
        db.commit()
        cursor.close()

class MovieMongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("localhost",27017)
        db = client["movieSite"]
        self.MoviesiteItem = db["MoviesiteItem"]
    def process_item(self, item, spider):
        if isinstance(item, MoviesiteItem):
            try:
                self.MoviesiteItem.insert(dict(item))
            except Exception:
                pass
        return item

#
# CREATE TABLE `movie` (
#   `id` int(10) NOT NULL AUTO_INCREMENT,
#   `movieTitle` varchar(255) DEFAULT NULL,
#   `movieImgUrl` varchar(255) DEFAULT NULL,
#   `movieStatus` varchar(255) DEFAULT NULL,
#   `pushTime` datetime DEFAULT NULL,
#   `movieDetailUrl` varchar(255) NOT NULL,
#   `movieDetailDirect` varchar(255) DEFAULT NULL,
#   `movieDetailActors` longtext,
#   `movieDetailType` varchar(255) DEFAULT NULL,
#   `movieDetailRelease` varchar(255) DEFAULT NULL,
#   `movieDetailCountry` varchar(255) DEFAULT NULL,
#   `movieDetailLanguage` varchar(255) DEFAULT NULL,
#   `movieDetailGrade` varchar(255) DEFAULT NULL,
#   `movieDetailStory` longtext,
#   PRIMARY KEY (`id`,`movieDetailUrl`) USING BTREE
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;