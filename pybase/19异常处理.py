#
# try:
#     print("-------输入-------")
#     # 1 / 0
#     height = input("请用户输入身高单位m:")
#     height = float (height)
#     file =None
#     file=open("aaaa.txt","w")
#     file.write("你好")
#     print("---------输入----------")
#     file.close()
# except Exception as e:
#     print(e)
#     print("请输入您的身高比如1.78")
# else:
#     print("哈哈没有异常")
#
# finally:
#     if file is not None:
#         file.close()
#     print("我是finally 我被执行了")


def test1():     # 这个不能运行,举的异常例子

    print("----test1-1----")
    print(num)
    print("----test1-2----")

def test2():     # 这个不能运行,举的异常例子
    print("----test2-1----")
    test1()
    print("----test2-2----")

def test3():     #这个用来捕获异常的例子
    try:
        print("----test3-1----")
        test1()
        print("----test3-2----")
    except Exception as result:
        print("捕获到了异常，信息是:%s"%result)
        print("----test3-3----")
    finally:
        print('晚安~')
# test3()
# print("------华丽的分割线-----")
# test2()

# test2()
test3()

# 异常处理
try:
    try:
        100+'你好'
    except:
        print("出现异常了")

    1/0
except:
    print("分母不为零")
finally:
    print("收尾工作")



# # goto语句
# try:
#     while True:
#         while True:
#             for i in range(10):
#                 if i >3:
#                      # raise
#                 print(i)
#             print("被跳过")
#         print("被跳过")
#     print("被跳过")
# except:
#     print("到这来了~")


