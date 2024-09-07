# lst1 =[11,22,33]
# lst2 = [22,33,44]
# for i in lst1:
#     if i in lst2:
#         print(i)
#
#
# # 6.要求：定义一个函数，能够输出自己的姓名和年龄，并且调用这个函数让它执行
# #
# # 使用def定义函数
# # 编写完函数之后，通过 函数名() 进行调用
# def name_info(name,age):
#
#     print("您的姓名是:",name)
#     print("您的年龄是:",age)
#
# name_info("胖达",18)
#
# # 3.给用户9次机会 猜1 - 10 个数字随机来猜数字。
# # 如果随机的数字和用户输入的数字一致则表示正确，如果不一致则表示错误。最终结果要求用户怎么也猜不对
import random
def choujiang(user):
# 1.循环九次
    if user.isdigit ():
        user = int ( user )
        if 0 < user <= 10:
            computer = random.randint ( 1, 10 )

            # 4.判断 输入==随机 正确
            if user == computer:
                print ( "恭喜你中奖了" )
            # 5.判断不一致 错误
            else:
                print ( "计算机的随机数字为:", computer )
                print ( "很遗憾,未中,请继续充值" )
        else:
            print("请输入1-10之间的数字")
    else:
        print("请输入1-10之间的数字")
choujiang("5")
# i=1
# while i<10:
#     # 2.输入1-10的数字
#     user=input("抽奖游戏,请输入1-10数字,输入0退出:")
#
#     # 3生成随机数字
#
#
#
#
# # 6.用户不能正确