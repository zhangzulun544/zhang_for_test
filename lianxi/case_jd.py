import unittest
from selenium import webdriver
from sle.setting import DB, t_class_sle
import time

i = DB.DB()                     #实例化sql

sql = i.find(['*','test_case'])                     #查询语句
driver = webdriver.Firefox()                        #使用火狐驱动
driver.get("https://www.jd.com/")                   #打开开始操作的页面
d = t_class_sle.All_set(driver)                     #实例化selenium的驱动参数
# d.action(["xpath","//*[@id='J_mobile']/div[1]"])


class Test_1(unittest.TestCase):                    #定义测试类

    def test_find(self):
        for c in sql:
            print(c)
            time.sleep(1)
            list_1 = c[1].split(",")
            d.type(list_1, c[3])
            list_2 = c[2].split(",")
            print(list_2[0:2])
            d.click(list_2[0:2])
            d.click(list_2[2:])
            time.sleep(2)
            t = d.find_element(["xpath","/html/body/div[6]/div[2]/div[1]/div[3]/div/div[2]/div[1]/ul/li[1]/a"]).text
            self.assertEqual(t,c[4])
            d.back()
            d.back()
        d.quit()

if __name__ == "__main__":

    unittest.main()
#
# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()
#
# driver.get("https://www.jd.com/")
#
# # 获得当前窗口句柄
# #sreach_windows = driver.current_window_handle
# driver.find_element_by_link_text("优惠券").click()
#
# #这里不加等待时间，下一步的获取所有窗口有时只能获取到一个
# time.sleep(3)
#
# # 获得当前所有打开的窗口的句柄
# all_handles = driver.window_handles
# print(all_handles)
#
# #切换第二个窗口
# driver.switch_to.window(all_handles[1])
# print('now register window!')
# driver.find_element_by_xpath("//*[@id='ttbar-apps']/div[1]/a").click()
# time.sleep(2)
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# driver = webdriver.Firefox()
# driver.implicitly_wait(10)
# driver.get('http://www.baidu.com')
#
# # 鼠标悬停至“设置”链接
# link = driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(link).perform()
#
# # 打开搜索设置
# driver.find_element_by_link_text("搜索设置").click()
#
# # 保存设置
# driver.find_element_by_class_name("prefpanelgo").click()
# time.sleep(2)
#
# # 接受警告框
# driver.switch_to.alert.accept()
#
# driver.quit()

