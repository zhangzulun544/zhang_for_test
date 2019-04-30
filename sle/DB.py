import pymysql

class DB(object):
    def __init__(self):                #连接
        self.db = pymysql.connect(host="localhost",user="root", password="zhang523", port=3307,db="test")

    def comit(self):                #提交
        self.db.comit()

    def close(self):               #断开数据库连接
        self.db.close()

    def find(self,a):               #查询语句定义
        with self.db.cursor() as cursor:                       #创建游标查询
            sql = "select %s from %s"
            cursor.execute(sql%(a[0],a[1]))
            x = cursor.fetchall()
            return x

    def add(self,tu):                       #插入语句定义
        tu_1 = str(tu[0])
        tu_2 = str(tu[1])
        sql = "insert into %s values(%s)"%(tu_1,tu_2)  #根据需求来改 ,UI自动化用不怎么到
        self.db.cursor(sql).execute()
