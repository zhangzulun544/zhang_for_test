import yaml
import pytest
from tytest.ty_setting import login, req
import logging
fname = open(r'C:\Users\boxun\PycharmProjects\zhang_for_test\sle\config\sle_new_purchase_order.yaml',encoding='utf-8')
case = yaml.load(fname,Loader=yaml.FullLoader)


def test_select():                          #进销查询接口测试
    assert login.login()["code"] == "000000"
    for y in case:
        url ,data,method = y["url"],y["data"],y["method"]
        order = req.req(url=y['url'], data=y['data'], method=y['method'])
        assert order[y["rp"]] == y["check"]


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])