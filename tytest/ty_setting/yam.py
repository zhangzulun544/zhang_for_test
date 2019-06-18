import yaml
#调试用例
f = open(r'C:\Users\boxun\PycharmProjects\zhang_for_test\tytest\case\oder.yaml',encoding="utf-8")
y = yaml.load(f,Loader=yaml.FullLoader)
x = y[0]["data"]
print(x)