# 1.现在有 a = [1,2,3,4,5,6] 不通过函数的形式实现列表的反转([6,5,4,3,2,1])
a = [1,2,3,4,5,6]
a.reverse()
a[::-1]


# 2.用pop()方法取出a列表里的最后一个元素，再加入到b列表里
temp = a.pop(5)

b = []
b.append(temp)


# 3.给用户9次机会 猜1 - 10 个数字随机来猜数字。
# 如果随机的数字和用户输入的数字一致则表示正确，如果不一致则表示错误。最终结果要求用户怎么也猜不对

# 抽奖  给我一个1-10的数 看看你的手气有没有中奖
# import random
# def chou_jiang(user,range):
#     # 3.生成随机数字
#     if user.isdigit():
#         user = int(user)
#         # nums.remove(user)
#         # computer = random.choice(nums)
#         if 0 < user <= range:
#             computer = random.randint(1, range)
#             # 4.判断 输入==随机 正确
#             # 5.判断不一致 就错误
#             while user == computer:
#                 computer = random.randint(1, range)
#             if user == computer:
#                 computer += 1
#
#             if user == computer:
#                 print("恭喜你中奖了")
#             else:
#                 print("系统随机的数字是:", computer)
#                 print("很遗憾,没有中,请继续充值")
#
#         else:
#             print("请输入1-%s之间的数字" % range)
#
#     else:
#         print("请输入1-%s之间的数字" % range)

import random

def chou_jiang(user,range,percent):

    if user.isdigit():
        user = int(user)
        if 0 < user <= range:
            num = user * percent/100
            computer = random.randint(1, range)

            if user == computer:
                print("恭喜你中奖了")
            else:
                print("系统随机的数字是:", computer)
                print("很遗憾,没有中,请继续充值")
        else:
            print("请输入1-%s之间的数字" % range)
    else:
        print("请输入1-%s之间的数字" % range)
num = input("请输入1-20之间的数:")
chou_jiang(num,20,50)


# 4.有两个列表 lst1 = [11, 22, 33] lst2 = [22, 33, 44]获取内容相同的元素
# lst1 = [11, 22, 33]
# lst2 = [22, 33, 44]
# for i in  lst1:
#     if i in lst2:
#         print(i)


#5.列表遍历使用while

# 6.要求：定义一个函数，能够输出自己的姓名和年龄，并且调用这个函数让它执行
#
# 使用def定义函数
# 编写完函数之后，通过 函数名() 进行调用

# def name_info(name,age):
#     print("您的姓名是:",name)
#     print("您的年龄是:",age)
#
# name_info("胖达",18)
