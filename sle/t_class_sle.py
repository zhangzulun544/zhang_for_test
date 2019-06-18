#————————————————————测试基类封装——————————————————————————————————————
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains                #鼠标包
# from selenium.webdriver.support import expected_conditions as EC              #显式等待包
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
import time
from time import ctime


class All_set(object):

    #封装selenium的元素定位和其他功能，具体根据不同业务来定
    def __init__(self,driver):
        # 定义基本驱动参数
        self.driver = driver
        # 设置8种selenium中的定位类型作为列表，下面做判断
        self.all_list = ["id", "name", "class", "tag", "link", "plink", "css", "xpath"]

    #寻找页面元素的8种方法，根据传的selector参数（list）来判断
    def find_element(self,selector):
        self.driver.implicitly_wait(10)
        by = selector[0]
        value = selector[1]
        element = None
        if by in self.all_list:
            try:
                print(ctime())
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
            finally:
                print(ctime())
        else:
            logging.error("输入的元素定位方式错误")

    #键入输入框内容
    def type(self,selector,value):
        element = self.find_element(selector)
        # element.clear()
        #logging.info("清空输入内容")
        try:
            element.send_keys(value)
           # logging.info("输入的内容%s"%value)
        except BaseException:
            logging.error("输入的内容错误")

    #点击
    def click(self,selector):
        element = self.find_element(selector)
        try:
            element.click()
        except BaseException:
            logging.error("点击错误")

    def submit(self,selector):
        element = self.find_element(selector)
        element.submit()

    #强制暂停
    # def sleep(self,seconds):
    #     time.sleep(seconds)
    #     logging.info("暂停%s秒"%seconds)

    #关闭网页
    def quit(self):
        self.driver.quit()
        logging.info("关闭浏览器")

    def close(self):
        self.driver.close()
        logging.info("关闭单个窗口")

    #后退
    def back(self):
        self.driver.back()
        logging.info("后退")

    #前进
    def forward(self):
        self.driver.forward()
        logging.info("前进")

    #刷新
    def refresh(self):
        self.driver.refresh()
        logging.info("刷新")

    # 设置网页窗口尺寸，没啥用
    def windows(self,c,k):
        self.driver.set_window_size(c,k)

    #切换窗口,返回所有窗口一个list
    def windows_handle(self,handle):
        all_windows = self.driver.window_handles
        return all_windows

    #鼠标悬停
    def action(self,selector):
        adove = self.find_element(selector)
        ActionChains(self.driver).move_to_element(adove).perform()

    #隐式等待
    def implicitly(self,time):
        self.driver.implicitly_wait(time)


    #显式等待
    # def wait(self):
    #     element = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(By.ID,"key"))

