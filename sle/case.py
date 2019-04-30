import unittest
from sle import t_class_sle
from selenium import webdriver
from openpyxl import load_workbook
from sle import DB
i = DB.DB()
sql = i.find(['*','test_case'])



driver = webdriver.Firefox()
driver.get("https://www.jd.com/")
d = t_class_sle.All_set(driver)


class test_1(unittest.TestCase):

    def test_find(self):
        for c in sql:
            d.sleep(1)
            list_1 = c[1].split(",")

            d.type(list_1, c[4])
            list_2 = c[2].split(",")
            print(list_2)
            d.click(list_2)
            t = d.find_element(["css","html body div#J_searchWrap.w div#J_crumbsBar.crumbs-bar div.crumbs-nav div.crumbs-nav-main.clearfix div.crumbs-nav-item strong.search-key"]).text
            self.assertEqual(eval(t),c[3])
            d.back()


if __name__ == "__main__":

    unittest.main()
