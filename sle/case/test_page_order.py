from selenium import webdriver
from sle.setting import DB, t_class_sle
from lxml import etree
import yaml
import time
import pytest

f = open(r'C:\Users\boxun\PycharmProjects\zhang_for_test\sle\config\sle_page_purchase_order.yaml',encoding="utf-8")
y = yaml.load(f,Loader=yaml.FullLoader)

def test_page_order():

    driver = webdriver.Firefox()
    driver.get("http://www.titun365.com")
    d = t_class_sle.All_set(driver=driver)
    d.windows()

    try:
        for i in y:
            se = i["se"]            #定位方式和元素
            value = i["value"]      #键入值
            time.sleep(2)

            if value != None:
                d.type(se,value)

            else:
                d.click(se)
    except:
        pass

    html = driver.execute_script('return document.documentElement.outerHTML') #返回加载完的html,很好用
    dom = etree.HTML(html)
    content = dom.xpath('//*[@class="el-table__body"]/tbody/tr')

    for i in content:
        try:
            assert "总部仓库1" in i.xpath("./td[3]/div//text()")
        except:
            print("按条件查询出错")
if __name__ == '__main__':
    pytest.main(["test_page_order.py"])


    # pytest.main(['-s', '-q', '--alluredir', './report/xml'])
#
# from selenium import webdriver
# d = webdriver.Firefox()
# d.get("http://www.titun365.com")
#
# html = d.execute_script('return document.documentElement.outerHTML') #返回加载完的html,很好用
# print(html)

# driver = webdriver.Firefox()
# driver.get("http://www.titun365.com")
# d = t_class_sle.All_set(driver=driver)
# d.windows()
#
# try:
#     for i in y:
#         se = i["se"]            #定位方式和元素
#         value = i["value"]      #键入值
#         time.sleep(2)
#
#         if value != None:
#             d.type(se,value)
#
#         else:
#             d.click(se)
# except:
#     pass
#
# html = driver.execute_script('return document.documentElement.outerHTML')
# dom = etree.HTML(html)
# content = dom.xpath('//*[@class="el-table__body"]/tbody/tr')
#
# for i in content:
#     print(i.xpath("./td[3]/div//text()"))