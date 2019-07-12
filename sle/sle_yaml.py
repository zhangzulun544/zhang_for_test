import yaml
#调试用例
f = open(r'C:\Users\boxun\PycharmProjects\zhang_for_test\sle\sle_login_case.yaml',encoding="utf-8")
y = yaml.load(f,Loader=yaml.FullLoader)

# print(x)
# print(type(x[0][0]))
#
# def ya():
#     for u in y:
#        for i in u:
#            if "se" in i:
#                yield i
#
#            elif "value" in i:
#                yield i

# def na(se,va):
#     return se["se"],va["value"]
#
# for i in y:
#     print(na(i[0],i[1]))
    # cs = list(map(na(i[0],i[1]),i))
    # print(cs)
# l = []
# def zhan():
#     for i in y:
#         l.append(i)
#         yield l[0]
#         l.pop()
#
# x = zhan()




for i in y:
    print(i)
    break