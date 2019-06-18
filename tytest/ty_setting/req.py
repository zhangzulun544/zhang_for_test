import requests
import json

r = requests.Session()

m_url = "http://192.168.1.106:9528"  # 环境


def req(url, data, method):  # 请求方法，根据metho判断请求方式

    if method == "post":
        re = r.post(url=m_url + url, data=data)
        try:
            re.raise_for_status()
            js = json.loads(re.text)
            return js
        except:
            print("请求失败")
            return re.status_code
    else:
        re = r.get(url=m_url + url, data=data)
        try:
            re.raise_for_status()
            js = json.loads(re.text)
            return js
        except:
            print("请求失败")
            return re.status_code