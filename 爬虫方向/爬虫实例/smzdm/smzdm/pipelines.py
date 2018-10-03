# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from smzdm.items import SmzdmItem
import pymongo
import pymysql

class SmzdmMySQLPipeline(object):
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
            insert into smzdm(
                id,title,href,referrerName,starNum,againStarNum,pushTime,fromWhere
              ) 
              values(null,%s,%s,%s,%s,%s,%s,%s);
        """
        cursor.execute(sql,[item['title'],item['href'],item['referrerName'],item['starNum'],item['againStarNum'],item['pushTime'],item['fromWhere']])
        db.commit()
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