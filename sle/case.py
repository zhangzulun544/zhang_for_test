import unittest
from sle import t_class_sle
from selenium import webdriver
from openpyxl import load_workbook
from sle import DB

i = DB.DB()                     #实例化sql

sql = i.find(['*','test_case'])                     #查询语句
driver = webdriver.Firefox()                        #使用火狐驱动
driver.get("https://www.jd.com/")                   #打开开始操作的页面
d = t_class_sle.All_set(driver)                     #实例化selenium的驱动参数


class Test_1(unittest.TestCase):                    #定义测试类

    def test_find(self):
        for c in sql:
            d.sleep(1)
            list_1 = c[1].split(",")
            d.type(list_1, c[3])
            list_2 = c[2].split(",")
            print(list_2[0:2])
            d.click(list_2[0:2])
            d.click(list_2[2:])
            d.sleep(2)
            t = d.find_element(["xpath","/html/body/div[6]/div[2]/div[1]/div[3]/div/div[2]/div[1]/ul/li[1]/a"]).text
            self.assertEqual(t,c[4])
            d.back()
            d.back()


if __name__ == "__main__":

    unittest.main()
