import pymysql
import pymongo
from gysta.items import GystaItem

class GystaPipeline(object):
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
        print(item['TOURNAME'])
        sql = """
            insert into em_tours(
                ID,TOURNAME,TOURTYPE,TOURTYPE1,TOURNUM,ORIGIN,TOURLINE,HOTEL,STARTDATE,ENDDATE,AMOUNT,STATUS
              )
              values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        data = [item['TOURNAME'],item['TOURTYPE'],item['TOURTYPE1'],item['TOURNUM'],item['ORIGIN'],item['TOURLINE'],item['HOTEL'],item['STARTDATE'],item['ENDDATE'], item['AMOUNT'],item['STATUS'] ]
        print('++++++++++++++++++++++++++++++++++')
        print(data)
        cursor.execute(sql,data)
        db.commit()
        cursor.close()

    # def process_item(self, item, spider):
    #         db = pymysql.connect(
    #             host="127.0.0.1",
    #             user='root',
    #             password='admin123',
    #             database='pymysql',
    #             port=3306
    #         )
    #         cursor = db.cursor()
    #         sql = """
    #             insert into test(
    #                 ID,title
    #               )
    #               values(null,%s);
    #         """
    #         cursor.execute(sql,['liu'])
    #         db.commit()
    #         cursor.close()

class GystaMongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("localhost",27017)
        db = client["myDB"]
        self.GystaItem = db["em_tours"]
    def process_item(self, item, spider):
        if isinstance(item, GystaItem):
            try:
                self.GystaItem.insert(dict(item))
            except Exception:
                print("出错了++++++++++++++++++++++++++++++++++++++++++++++")
        return item


# mySQL 脚本
# CREATE TABLE `em_tours` (
#   `ID` int(10) NOT NULL AUTO_INCREMENT,
#   `AMOUNT` varchar(255) DEFAULT NULL,
#   `TOURNAME` varchar(255) DEFAULT NULL,
#   `BUSNUM` varchar(255) DEFAULT NULL,
#   `GUIDECARDNUM` varchar(255) DEFAULT NULL,
#   `TRAVELAGENCYCODE` varchar(255) DEFAULT NULL,
#   `STARTDATE` varchar(255) DEFAULT NULL,
#   `ENDDATE` varchar(255) DEFAULT NULL,
#   `DESTINATION` varchar(255) DEFAULT NULL,
#   `TOURNUM` varchar(255) DEFAULT NULL,
#   `TOURTYPE` varchar(255) DEFAULT NULL,
#   `SOURCE` varchar(255) DEFAULT NULL,
#   `STATUS` varchar(255) DEFAULT NULL,
#   `CSTATUS` varchar(255) DEFAULT NULL,
#   `REGION` varchar(255) DEFAULT NULL,
#   `TOURTYPE1` varchar(255) DEFAULT NULL,
#   `ORIGIN` varchar(255) DEFAULT NULL,
#   `TOURLINE` varchar(255) DEFAULT NULL,
#   `HOTEL` varchar(255) DEFAULT NULL,
#   PRIMARY KEY (`ID`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;