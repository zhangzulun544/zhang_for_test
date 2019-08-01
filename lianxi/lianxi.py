# l1 = [11,23,3,4,52]
#
# def findmaxandmin(l):       #用排序挑出最大和最小值
#     lenx = len(l)
#     for i in range(0,lenx):
#         for j in range(0,lenx-1):
#             if l[i]>l[j]:
#                 l[i],l[j] = l[j],l[i]
#
#     return (l[0],l[-1])

# def findmax(l):             #用赋值迭代比较挑出最大和最小值
#     le = len(l)
#     max = l[0]
#     min = l[0]
#
#     for i in l:
#         if i>max:
#             max = i
#         if i<min:
#             min = i
#
#     return (max,min)
#
# x = findmax(l1)
# print(x)
#
# x = findmaxandmin(l1)
# print(x)


# l1 = [x for x in range(1,199)]
# l2 = (x for x in range(1,20)) 生成器（generator）generator保存的是算法
# for i in l2:
#     print(i)

# def fib(max):
#     a,b,c = 0,0,1
#     while a<max:
#         yield c
#         a,c = c,a+c
#         a=a+1
#     return "done"
#
# for i in fib(6):
#     print(i*i)

# def yan():   #杨辉三角
#     l = [1]
#     while len(l)<2:
#         yield l
#         l = [l+[l[x]+l[x+1] for x in range(len(l)-1)]+l]
#     #这段逻辑是真的牛逼
#
# for i in yan():
#     print(i)



# def new(x,y,f):       高阶函数
#     return f(x)+f(y)
#
# f = len
# x = new([1],[1,4,2,3],f)
# print(x)


#  map    map函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# #################求一个数组每个值的积################
# l = [x for x in range(1,10)]
#
# #普通循环
# l2 = []
# for i in l:
#     l2.append(i*i)
# print(l2)
#
#换高阶函数写法：

# def f(x,y):
#     return x*y
# new = list(map(f,l))
# print(new)

# #第三种2层列表表达式
# te = [x*x for x in l]
# print(te)
#reduce

# from functools import reduce
#
# def add(x,y):
#     return x+y
#
# def fn(f):
#     return f*f
#
# fx = list(map(fn,[1,3,5,7,9]))
# print(fx)
# af = reduce(add,fx)
#
# print(af)

# l = [x for x in range(1,5)]
# x = reduce(add,l)
# ma = list(map(add,l))

# print(x)
# print(sum(l))
# print(ma)

# #查找A字符串中的在b中有多少个
# class Solution(object):
#     def numJewelsInStones(self, J, S):
#         count = 0
#         for x in J:
#             count += S.count(x)
#         print(count)
# x = Solution()
# x.numJewelsInStones("aA","aAAbbbb")

#大小写转化
# class Solution(object):
#     def toLowerCase(self, str):
#         x = str.lower() #   str.uuper（)
#         return x

# def normalize(name):  #不规范的英文名字，变为首字母大写
#     return name.capitalize()
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

#  filter       根据第一个参数（自定义函数），判断第二个参数（可迭代数据类型），将返回结果为True的保留下来（结果是迭代器）

# def f(x):
#     return x%2 != 1
# x = list(filter(f,[1,2,3,4,5,6,7,8]))
# print(x)

#sorted         第一个参数为list，第二个key，keykey加自定义的函数或内置函数，对list中的每个值顺序进行映射,在sorted方法中进行比较后，输入对应的结果

# x = sorted(['Credit', 'Zoo', 'about', 'bob'],key=str.upper,reverse=True)
# print(x)

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# def by_name(t):
#     return t[0]
#
# def by_sort(t):
#     return t[1]
# x = sorted(L,key=by_name)
# x = sorted(x,key=by_sort)
# print(x)

#闭包         一个函数返回另一个函数

#构建一个求和函数
# def lazy_sum(*kw):
#     def sum():
#         ax = 0
#         for i in kw:
#             ax = ax + i
#         return ax
#     return sum
#
#
# x = lazy_sum(*[1,23,4])
# print(x())

#匿名函数

# x = list(filter(lambda x:x%2==1,range(1,100)))
# print(x)
# #等同于下面的,对比后代码更简洁
# l = []
# for i in range(1,100):
#     if i%2 ==1:
#         l.append(i)
# print(l)
#
#斐波那契数列
# def fib(num):
#     result = [0,1]
#     for i in range(num-2):
#         result.append(result[-2]+result[-1])
#     return result
#
# x = fib(10)
# print(x)

# from sle import DB
#
# Sql = DB.DB()
# find_purchase_order = ["*","`bill_purchase_order` order by gmt_create desc LIMIT 1;"]
# results = Sql.find(find_purchase_order)
# for r in results:
#     print(r[1])

#.//*[@class="el-table__row"][1]/td[3]/div


# import json
# import requests
# from functools import reduce
# re = requests.Session()
# login = re.post(url="http://www.titun365.com/login/login.json",data={"phone":"18258229393","password":"123456"})
# results = re.get(url="http://www.titun365.com/billPurchaseOrder/selectBillPurchaseOrderById.json?id=1234",data={"id":"1234"})
# js = json.loads(results.text)
# # print(js["data"]["detailList"][1]["hasInCount"])
#
# def cut(x,y):
#     return x-y
# li = []
# for i in js["data"]["detailList"]:
#     c = cut(i["notInCount"],i["hasInCount"])
#     li.append(abs(c))
#
# def add(x,y):
#     return x+y
#
# ad = reduce(add,li)
# print(ad)

# def high(x,y,f):         传入函数
#     return f(x+y)
#
# f = abs
# x = -100
# y = 2
#
# print(high(x,y,f))


# #普通筛选
# l = []
# for i in range(1,101):
#     if i%2 ==1:
#         l.append(i)
# print(l)
# #高级方法filter筛选
# def ou(x):
#     return x % 2 ==1
# y = list(filter(ou,[x for x in range(1,101)]))
# print(y)
# #列表表达式筛选
# y2 = [x for x in range(1,101) if x%2==1]
# print(y2)
# #加匿名函数的filte筛选
# y3 = list(filter(lambda x:x%2==1,[x for x in range(1,101)]))
# print(y3)



from lxml import etree
import json
import requests


# se = requests.Session()
# login = se.post(url="http://192.168.1.15:9528/stewards/login/login.json",data={"phone":18296477676,"password":123456})
#
# re = se.post(url="http://192.168.1.15:9528/stewards/clothesManage/selectBorrowOrReturnRecordList.json",
#                          data={"goodsName":None,"condition":None, "type":15,"startTime":None,"endTime":None,"pageSize":10,"pageNum":1})
#
# ge = se.get(url="http://192.168.1.15:9528/stewards/sysWarehouse/selectWareHoseSelect.json")
# js = json.loads(re.text)
# print(ge.text)