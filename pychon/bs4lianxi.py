# import requests
# from bs4 import BeautifulSoup
# # re = requests.get(url="https://python123.io/ws/demo.html")
# # demo = re.text
# # with open("demo.html","w") as f:
# #     f.write(re.text)
# #     f.close()
#
# soup = BeautifulSoup(open("demo.html"),"html.parser")   #html.parser的html的解析器，其他对应的有lxml。   xml。html5lib
# # print(soup.prettify())
#
#
# for link in soup.find_all(attrs="course"):                                 #find_all搜索括号内内容  参数：name.attrs,recursive,string,**kwargs
#     print(link)                                     #get,提取括号内内容

#练习实例
import requests
from bs4 import BeautifulSoup

re = requests.get(url="http://www.dili360.com/gallery/cate/1.htm")
soup = BeautifulSoup(re.text,"html.parser")
lis = []
for link in soup.body.find_all(name="img"):
    lis.append(link.get("src"))
print(lis)

def re_img(url):
    try:
        re = requests.get(url)
        re.raise_for_status()
        re.encoding = re.apparent_encoding
        name = url.split("/")[-1]
        name_j = name.split(".")[0]
        with open("D://JPG/%s.jpg"%(name_j),'wb') as f:
            f.write(re.content)
    except:
        print("爬取失败")

for i in lis:
    re_img(i)
