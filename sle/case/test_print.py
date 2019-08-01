from selenium import webdriver
from sle.setting import DB, t_class_sle
from lxml import etree
import yaml
import time
import pytest

f = open(r'C:\Users\boxun\PycharmProjects\zhang_for_test\sle\config\sle_print.yaml',encoding="utf-8")
y = yaml.load(f,Loader=yaml.FullLoader)

def test_page_order():

    driver = webdriver.Firefox()
    driver.get("http://192.168.1.15:9528")
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

    d.close()

if __name__ == '__main__':
    pytest.main(["test_print.py"])
#单独的打印不包含建采购单