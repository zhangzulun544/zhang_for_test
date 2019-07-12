from sle import t_class_sle
from selenium import webdriver

diver = webdriver.Firefox()
diver.get("http://192.168.1.106:9528")

c = t_class_sle.All_set(diver)
for i in range(1,1000):#暴力点击
    c.click(["css","html body div#app section.el-container.login-container.is-vertical main.el-main div.login-form div.login-way form.el-form.el-form--label-left div.el-form-item div.el-form-item__content button.el-button.el-button--primary"])

diver.quit()