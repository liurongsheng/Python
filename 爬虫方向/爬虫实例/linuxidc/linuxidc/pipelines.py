import pymysql

class MySQLPipeline(object):
    db = pymysql.connect(
        host="127.0.0.1",
        user='root',
        password='admin123',
        database='pymysql',
        port=3306
    )

    def __init__(self):
        cursor = self.db.cursor()
        cursor.execute("DROP TABLE IF EXISTS LINUXIDC")
        sqlinit = """CREATE TABLE LINUXIDC (
             id int(20) NOT NULL AUTO_INCREMENT,
             bookName varchar(256),
             bookPushTime varchar(256),
             downloadUrl varchar(256),
             PRIMARY KEY (`id`) USING BTREE
             ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=UTF8MB4;
         """
        cursor.execute(sqlinit)
        self.db.commit()
        cursor.close()

    def process_item(self, item, spider):
        cursor = self.db.cursor()
        sql = """
            insert into LINUXIDC(
                id,bookName,bookPushTime,downloadUrl
              )
              values(null,%s,%s,%s);
        """
        cursor.execute(sql,[item['bookName'], item['bookPushTime'], item['downloadUrl']])
        self.db.commit()
        cursor.close()
