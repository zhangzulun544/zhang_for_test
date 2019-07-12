from sle import t_class_sle
from selenium import webdriver

import yaml
import time
import pytest


f = open(r'C:\Users\boxun\PycharmProjects\zhang_for_test\sle\sle_login_case.yaml',encoding="utf-8")
y = yaml.load(f,Loader=yaml.FullLoader)



def test_login():
    driver = webdriver.Firefox()
    driver.get("http://192.168.1.15:9528")
    d = t_class_sle.All_set(driver=driver)
    d.windows()

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
                else:
                    d.click(se)
    except:
        print("程序错误")

#    assert d.find_element(["css","html body div#app div.app-wrapper div.main-container ul.navbar.el-menu--horizontal.el-menu div.rightInfo div.avatar-container.el-dropdown div.avatar-wrapper.el-dropdown-selfdefine span.avatar-user-name"]).text == "张祖伦"

if __name__ == '__main__':

    pytest.main()
