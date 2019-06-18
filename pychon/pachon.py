# import requests
# import json
#
# def re(url,p,head):
#     try:
#         re = requests.get(url=url,params=p,headers=head)
#         re.raise_for_status()
#         re.encoding = re.apparent_encoding
#         return re.text
#     except:
#         return "出现异常"
#
# if __name__ == "__main__":
#     url = "http://www.baidu.com/s"
#     he  = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
#     pa = {"wd":"python"}
#     r = re(url=url,p=pa,head=he)
#     #js = json.load(r)
#     print(r)

# import requests
# # import json
# #
# # url="https://github.com/session"
# # data={"commit":"Sign in","utf8":"✓","authenticity_token":"NME623EBRZruphV6vuOKWXaUYG+VlKQR1JtIstJbnv2befcVNPt5rHlfWlfm2Sw8h4rgKbk0hVuC4LyU91erIg==","login":"zhangzulun@163.com","password":"zhang523","webauthn-support":"supported"}
# # #登录后存cookie
# # head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
# # # check = s.post(url="http://www.titun365.com/stockCheckBill/selectStockCheckBillOrderById.json",data={"id":125},headers=head)
# # try:
# #     s = requests.Session()  # 带session的请求方法
# #     re = s.post(url, data,headers=head)
# #     print(re.status_code)
# # except:
# #     print("请求失败")


import requests
import bs4
from bs4 import BeautifulSoup

def Gethtml(url):
    r = requests.get(url=url,timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def Falllist(unlist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.tag):
            tds = tr('td')
            unlist.append([tds[0].string,tds[1].string,tds[2].string])



def Printhtml(unlist,num):
    pass

def main():
    unlist = []
    tag = Gethtml(url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html")
    Falllist(unlist,tag)
    Printhtml(unlist,20)
