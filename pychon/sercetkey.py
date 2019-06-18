import requests
from bs4 import BeautifulSoup

# def re(url):
#     try:
#         s = requests.Sessions()
#         data =
#         r = requests.get(url)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         print("爬取失败")
#
# all_url = "https://github.com/search?q=consume_user_resource_percent&type=Code"
#
# r = re(all_url)
# print(r)
# soup = BeautifulSoup(r,"html.parser")
# # for s in soup.find_all(string="privateKey"):
# #     print(s.get("span"))
# print(soup.find_all(string="privateKey"))

head = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'Cookie':'',
'Host':''
}

params = {'q':'consume_user_resource_percent','type':'Code'}

all_url = "https://github.com/search?q=consume_user_resource_percent&type=Code"

try:
    key  = requests.get(url=all_url,headers=head,params=params)
    key.raise_for_status()
    key.encoding = key.apparent_encoding
    with open('test.html','w') as f:
        f.write(key.text)
except:
    print("爬取失败")

# soup = BeautifulSoup(open("test.hrml",))