
# 1、
# "username"
# 对应为大驼峰和小驼峰命名为？
#
#
# 2、
# 写出python中5种简单数据类型？
#
#
# 3、
# 请写出四个python关键字？
# if else is in not while break continue
#
# 4、
# 在python中，9 % 2
# 输出结果为？
# 1
# print(9 % 2)
#
#
# 5、
# 如何把
# "77"
# 转换为int类型？
# int("77")
#
# 6、
# Python中，如何查看“hello
# world”的数据类型？
# type()
#
# 7、
# A = "abcdefg"，如何使用索引分别取出字符串A中的a和f字符
# A[0] A[5]
# 8、
# str2 = 'suensoem'，求出字符串str2的长度？
# len(str2)
#
# 9、
# 如何用字符串方法获取a在str1 = 'bcda'
# 中的索引值?
# str1.find("a") str1.index("a")
#
# 10、
# List2 = ["aaa", "bbb", "ccc", "ddd"]
# str1 = "eee"
# list3 = ["eee","fff"]
# 请用代码实现把字符串str1添加到列表List2中？
# append insert extend
#
# 11、
# list1 = ["aaa", "bbb", "ccc"]，删除list1中
# "bbb"?
#  pop remove del
#
#
# 12、
# dict1 = {"a": 1, "b": 2, "c": 3}, 请取出dict1中
# "c"
# 的值？ dict1["c"] dict1.get("c")
#
#
# 13、
# dict1 = {"a": 1, "b": 2, "c": 3}，使用字典的什么方法可以列表形式输出dict1中所有键?
# dict1.keys() dict1.values()  dict1.items()
#
# 14、
# a = 100，b = 200，定义一个函数，求出a * b的值？
# def multi(a=100,b=200):
#     # a =100
#     # b=200
#     return a*b

# multi(100,200)
# multi()
#
#
# 15、
# 封装一个函数： a.如果不是数字：则直接返回“不是数字，请重新输入” b.判断用户输入是否是数字，
# 如果是数字：则继续判断, 输入数字是否是9的倍数
# I.如果是，返回结果
# "是"， II.否则返回结果
# "否
# def is9num(num):
#     if num.isdigit():
#         num = int(num)
#         if num % 9 ==0 and num != 0:
#             return "是"
#         else:
#             return "否"
#     else:
#         return "不是数字，请重新输入"
#
#
# print(is9num("aaa"))

#
# 16、
# 编写一个函数，求1到100之间的奇数和？
# i = 1
# sum = 0
# while i <100:
#
#     if i %2 ==1:
#         sum += i
#     i +=1

# while i < 100:
#     sum += i
#     i += 2
# #
# 17、
# 通过循环创建十个文件，命名为1.txt，2.
# txt，3.
# txt....然后将文件名修改为：副本 - 1.
# txt，副本 - 2.
# txt，副本 - 3.
# txt...

import os

# def change_name():
#     if not os.path.exists("bb"):
#         os.mkdir("bb")
#
#     file_path ="./bb/"
#     try:
#         os.mkdir("bb")
#     except Exception as e:
#         pass
#
#     i = 1
#     while i <=10:
#         file = open(file_path+f"{i}.txt","w",encoding="utf8")
#         file.close()
#         i+=1
#
#     cpoy_str = "副本-"
#
#     # 1.txt --> 副本-1.txt
#     names = os.listdir(file_path)
#     for name in names:
#         new_name = cpoy_str+name
#         print(file_path+name)
#         print(file_path+new_name)
#         os.rename(file_path+name,file_path+new_name)


def change_name(num):
    # if not os.path.exists("bb"):
    #     os.mkdir("bb")

    file_path = "./bb/"
    # try:
    #     os.mkdir("bb")
    # except Exception as e:
    #     pass
    #
    # i = 1
    # while i <= 10:
    #     file = open(file_path + f"{i}.txt", "w", encoding="utf8")
    #     file.close()
    #     i += 1
    # 1.txt --> 胖达出品-1.txt
    # 1.txt --> 1-胖达出品.txt
    # aa.txt -->aa-胖达出品.txt
    cpoy_str = "-胖达出品"

    if num == "1":

        names = os.listdir(file_path)
        for name in names:
            new_name = cpoy_str + name
            print(file_path + name)
            print(file_path + new_name)
            os.rename(file_path + name, file_path + new_name)

    if num == "2":
        names = os.listdir(file_path)
        for name in names:
            name_list = name.split("-")
            print(name_list)
            os.rename(file_path+name,file_path+name_list[1])


def change_name2(num):
    # if not os.path.exists("bb"):
    #     os.mkdir("bb")

    file_path = "./bb/"
    # try:
    #     os.mkdir("bb")
    # except Exception as e:
    #     pass
    #
    # i = 1
    # while i <= 10:
    #     file = open(file_path + f"{i}.txt", "w", encoding="utf8")
    #     file.close()
    #     i += 1
    # 1.txt --> 胖达出品-1.txt
    # 1.txt --> 1-胖达出品.txt
    # aa.txt -->aa-胖达出品.txt
    cpoy_str = "-胖达出品"

    if num == "1":
        names = os.listdir(file_path)
        for name in names:
            if cpoy_str in name:
                return
            name_list = name.split(".")
            new_name = name_list[0]+cpoy_str+"."+name_list[1]
            print(file_path + name)
            print(file_path + new_name)
            os.rename(file_path + name, file_path + new_name)

    if num == "2":
        names = os.listdir(file_path)
        for name in names:
            if cpoy_str in name:
                # str_index = name.find(cpoy_str)
                # new_name = name[:str_index]+name[str_index+len(cpoy_str):]
                # name_list = name.split(cpoy_str)
                # print(name_list)
                # new_name= name_list[0]+name_list[1]

                new_name = name.replace(cpoy_str,"")
                print(new_name)
                os.rename(file_path + name, file_path + new_name)


# change_name2("2")



#
# 18、
# 面向对象
# a.在animal.py中创建一个Animal类，name属性设置传递参数，然后age属性设置为初始值为0，type属性设置为类属性值为狗;
# 设置一个实例方法eat()，打印狗吃骨头
# b.重新创建一个demo.py文件，引入animal模块，然后定义一个Dog类，继承Animal，重写里面的eat()，在原有基础上（狗吃骨头）, 添加打印内容;
# 吃完骨头摇摇头...;
#
# 19、
# 导入random模块, 生成1 - 100
# 间所有整数的随机列表(列表中的数字不重复, 长度为100)

# list_num = []
# import random
#
# while True:
#     num = random.randint(1,100)
#     if num not in list_num:
#         list_num.append(num)
#
#     if len(list_num) == 100:
#         break

# while len(list_num) <100:
#     num = random.randint(1,100)
#     if num not in list_num:
#         list_num.append(num)
#
# print(list_num)

#
# 20
# 选做题
# 使用循环:
# 输出九九乘法表
# 1 * 1 =1
# 1 * 2 =2 2 * 2=4
# 1 * 3 =3 2 * 3=6 3*3 =9
# 1 * 4 =4 2 * 4=8 3*4 =12 4*4=16

# 大循环是行,小循环是列
for i in range(1,10):
    # print(f"1 * {i} = {1*i}")
    for j in range(1,i+1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()


# 1 * 9 =9 2*9=18 3*9=27 4*9=36 5*9=45
# for j in range(1, 10):
#     print(f"{j} * 9 = {9 * j}", end="\t")
# print()
# for j in range(1, 10):
#     print(f"{j} * 9 = {9 * j}", end="\t")
# print()
# for j in range(1, 10):
#     print(f"{j} * 9 = {9 * j}", end="\t")
