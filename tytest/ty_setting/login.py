from tytest.ty_setting import req
import yaml

f = open(r'C:\Users\boxun\PycharmProjects\zhang_for_test\tytest\case\report.yaml',encoding="utf-8")
case = yaml.load(f,Loader=yaml.FullLoader)

def login():           #测试登录
    f = open(r'C:\Users\boxun\PycharmProjects\zhang_for_test\tytest\case\login.yaml',encoding="utf-8")
    y = yaml.load(f, Loader=yaml.FullLoader)
    loging = req.req(url=y["url"], data=y["data"], method=y['method'])
    return loging


