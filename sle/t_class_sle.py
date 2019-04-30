#————————————————————测试基类封装——————————————————————————————————————
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time


class All_set(object):
    #封装selenium的元素定位和其他功能，具体根据不同业务来定
    def __init__(self,driver):
        self.driver = driver                                                                    #定义基本驱动参数
        self.all_list = ["id", "name", "class", "tag", "link", "plink", "css", "xpath"]         #设置8种selenium中的定位类型作为列表，下面做判断
    def find_element(self,selector):
        by = selector[0]
        value = selector[1]
        element = None
        if by in self.all_list:
            try:
                if by == "id":
                    element = self.driver.find_element_by_id(value)
                elif by == "name":
                    element = self.driver.find_element_by_name(value)
                elif by == "class":
                    element = self.driver.find_element_by_class_name(value)
                elif by == "tag":
                    element = self.driver.find_element_by_tag_name(value)
                elif by == "link":
                    element = self.driver.find_element_by_link_text(value)
                elif by == "plink":
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == "css":
                    element = self.driver.find_element_by_css_selector(value)
                elif by == "xpath":
                    element = self.driver.find_element_by_xpath(value)
                else:
                    logging.error("没有找到原素")
                print('元素定位成功!定位方式：%s，使用的值%s：' % (by, value))
                return element
            except NoSuchElementException:
                logging.error("报错信息：",exc_info = 1 )
        else:
            logging.error("输入的元素定位方式错误")

    def type(self,selector,value):
        element = self.find_element(selector)
        # element.clear()
        #logging.info("清空输入内容")
        try:
            element.send_keys(value)
           # logging.info("输入的内容%s"%value)
        except BaseException:
            logging.error("输入的内容错误")

    def click(self,selecotor):
        element = self.find_element(selecotor)
        try:
            element.click()
        except BaseException:
            logging.error("点击错误")

    def sleep(self,seconds):
        time.sleep(seconds)
        logging.info("暂停%s秒"%seconds)

    def quit(self):
        self.driver.quit()
        logging.info("关闭浏览器")
    def back(self):
        self.driver.back()
        logging.info("后退")
    def forward(self):
        self.driver.forward()
        logging.info("前进")

    def refresh(self):
        self.driver.refresh()
        logging.info("刷新")

    def windows(self,c,k):              #设置网页窗口尺寸，没啥用
        self.driver.set_window_size(c,k)
# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from paly_new import dalong

# driver = webdriver.Firefox()
#
# driver.get("http://192.168.1.106:9528/#/login")
#
# print(driver.title)
#
# driver.find_element_by_name("phone").send_keys(18329039512)
# driver.find_element_by_name("password").send_keys("654321")
# time.sleep(3)
# denglu = driver.find_element_by_xpath("//*[@id='app']/section/main/div/div[2]/form/div[4]/div/button/span")
# ActionChains(driver).click(denglu).perform()                                                                              #傻吊式登录操作
