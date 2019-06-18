import yaml
from tytest.ty_setting import login, req

fname = open(r'C:\Users\boxun\PycharmProjects\zhang_for_test\tytest\case\oder.yaml',encoding='utf-8')
case = yaml.load(fname,Loader=yaml.FullLoader)


def test_newbiloder():                          #新建采购单
    assert login.login()["code"] == "000000"
    for y in case:
        url ,data,method = y["url"],y["data"],y["method"]
        order = req.req(url=y['url'], data=y['data'], method=y['method'])
        assert order["msg"] == "成功"
