from smzdm.items import SmzdmItem
import pymongo
import pymysql

class SmzdmMySQLPipeline(object):
    db = pymysql.connect(
        host="127.0.0.1",
        user='root',
        password='admin123',
        database='pymysql',
        port=3306
    )

    def __init__(self):
        cursor = self.db.cursor()
        cursor.execute("DROP TABLE IF EXISTS SMZDM")
        sqlinit = """CREATE TABLE SMZDM (
             id int(20) NOT NULL AUTO_INCREMENT,
             title varchar(256),
             href varchar(256),  
             referrerName varchar(50),
             starNum int(20), 
             againStarNum int(20), 
             pushTime varchar(20), 
             fromWhere varchar(20),
             PRIMARY KEY (`id`,`href`) USING BTREE 
             ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         """
        cursor.execute(sqlinit)
        self.db.commit()
        cursor.close()

    def process_item(self, item, spider):
        cursor = self.db.cursor()
        sql = """
            insert into SMZDM(
                id,title,href,referrerName,starNum,againStarNum,pushTime,fromWhere
              ) 
              values(null,%s,%s,%s,%s,%s,%s,%s);
        """
        cursor.execute(sql,[item['title'],item['href'],item['referrerName'],item['starNum'],item['againStarNum'],item['pushTime'],item['fromWhere']])
        self.db.commit()
        cursor.close()

class SmzdmMongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("localhost",27017)
        db = client["zdm"]
        self.SmzdmItem = db["SmzdmItem"]
    def process_item(self, item, spider):
        if isinstance(item, SmzdmItem):
            try:
                self.SmzdmItem.insert(dict(item))
            except Exception:
                pass
        return item