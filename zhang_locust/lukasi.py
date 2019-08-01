from locust import HttpLocust,TaskSet,task
import pymysql


class DB(object):

    def __init__(self):                #连接
        self.db = pymysql.connect(host="localhost",user="root", password="zhang523", port=3307,db="bur724")

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






class Userbehavior(TaskSet):
    def login(self,phone):
        self.client.post(url="/stewards/login/login.json", data={"phone": phone, "password": "654321"})

    # @task(1)
    # def bur_index(self):
    #     self.client.post(url="/stewards/login/login.json",data={"phone":18329039512,"password":"654321"})
    def user_all(self):
        sql = DB()
        user = sql.find(["mobile","sys_user"])
        for i in user:
            for j in i:
                yield j
    @task
    def bur_kucun(self):
        # self.client.post(url="/stewards/admin/sysDistributor/selectDistributorList.json",
        #                  data={"condition": "", "companyName": "", "pageSize": 15, "pageNum": 1})
        for i in self.user_all():
            self.login(phone=i)
            self.client.get(url="http://192.168.1.15:9528/stewards/sysWarehouse/selectWareHoseSelect.json")


class WebsiteUser(HttpLocust):
    task_set = Userbehavior
    host = "http://192.168.1.15:9528"
    min_wait = 1000
    max_wait = 3000
