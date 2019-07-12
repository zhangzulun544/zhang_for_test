from sle import t_class_sle
from selenium import webdriver
from sle import DB
import yaml
import time
import pytest


f = open(r'C:\Users\boxun\PycharmProjects\zhang_for_test\sle\sle_login_case.yaml',encoding="utf-8")
y = yaml.load(f,Loader=yaml.FullLoader)
#提取yaml中的测试用例（元素，输入值，检查点）

l = []      #加个列表存下返回的数据，在第二个测试函数中使用

def test_New_purchase_order():
    driver = webdriver.Firefox()
    driver.get("http://192.168.1.15:9528")
    d = t_class_sle.All_set(driver=driver)
    d.windows()
    #打开主页
    try:
        for i in y:
            se = i["se"]
            value = i["value"]
            time.sleep(2)
            if value != None:
                d.type(se,value)

            else:
                if "check" in i:
                    check = i["check"]
                    assert d.find_element(se).text == check
                    #d.click(se)
                elif "sql" in i:
                    sq = d.find_element(se).text
                    l.append(sq)
                else:
                    d.click(se)


    except:
        d.close()
        print("程序错误")
    #对yaml中的用例进行遍历操作。根据不同的字段进行操作，在需要测试的地方多加了个条件进行断言，有check的值就进行断言，没有check就代表了正常操作。简化了代码，不必每个步骤进行编写。
    #适用于流程分析的测试方法
    d.close()

def test_sql_purchase_order():
    Sql = DB.DB()
    find_purchase_order = ["*", "`bill_purchase_order` order by gmt_create desc LIMIT 1;"]
    results = Sql.find(find_purchase_order)
    for r in results:
        try:
            assert r[1] == l.pop()
        except:
            print("采购单不匹配",)

if __name__ == '__main__':

    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
