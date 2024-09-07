# # 进入车站 通过安检 检票
#
# knife = 4
#
# piao = 1
#
# hesuan = 12
#
# if hesuan <= 48:
#     print("核算检测通过")
#     if knife < 5:
#         print("通过安检")
#
#         if piao == 1:
#             print("可以上火车")
#
#         else:
#             print("被从车上赶了下来")
#
#     else:
#         print("没有通过安检,被扭送进了派出所")
#
# else:
#     print("核算超过了48小时需要重新做")


# 包子 = 5
#
# 卖西瓜 = 1
#
# if 卖西瓜 == 1:
#     包子 = 1
#
# 生成 1 2 3随机数 随机生成123


import random
# 这里的随机数全是可以取到边界值的且是全闭区间,,跟定位有关的是左闭右开区间!!!!!!
num = random.randint(1,3)
if num==1:
    print(num)
else:
    for i in str(num):
        if i==2 or 3:
            print(i)
pass