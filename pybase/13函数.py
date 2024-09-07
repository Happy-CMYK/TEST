#
#
# # 有特定功能的代码块
#
# def print_fozu():
#     print("                            _ooOoo_  ")
#     print("                           o8888888o  ")
#     print("                           88  .  88  ")
#     print("                           (| -_- |)  ")
#     print("                            O\\ = /O  ")
#     print("                        ____/`---'\\____  ")
#     print("                      .   ' \\| |// `.  ")
#     print("                       / \\||| : |||// \\  ")
#     print("                     / _||||| -:- |||||- \\  ")
#     print("                       | | \\\\\\ - /// | |  ")
#     print("                     | \\_| ''\\---/'' | |  ")
#     print("                      \\ .-\\__ `-` ___/-. /  ")
#     print("                   ___`. .' /--.--\\ `. . __  ")
#     print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
#     print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
#     print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
#     print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
#     print("                            `=---='  ")
#     print("  ")
#     print("         .............................................  ")
#     print("                  佛祖镇楼                  BUG辟易  ")
#     print("          佛曰:  ")
#     print("                  写字楼里写字间，写字间里程序员；  ")
#     print("                  程序人员写程序，又拿程序换酒钱。  ")
#     print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
#     print("                  酒醉酒醒日复日，网上网下年复年。  ")
#     print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
#     print("                  奔驰宝马贵者趣，公交自行程序员。  ")
#     print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
#     print("                  不见满街漂亮妹，哪个归得程序员？")
#
# # 调用
# print_fozu()
#
# # print_fozu()
#
# # y = f(x)
#
# def add_cal(a,b):
#     # a = 10
#     # b = 20
#     # print("a的值为:",a)
#     # print("b的值为:",b)
#     c = a +b
#     # print(c)
#     return c
# a = input("请输入要计算的第一个值:")
# b = input("请输入要计算的第二个值:")
# a = int(a)
# b = int(b)
# print("a的值为:",a)
# print("b的值为:",b)
#
# res = add_cal(a, b)
# # 定义的函数需要几个参数就传几个 不能多传也不能少传
# # res = add_cal(10, 5)
# print(res)


# 匿名函数 不需要起名字
#  res =lambda x,y: x + y
# print(res(5,8))


# 获取函数以及函数对应的索引值(可以自定义索引值)
# test_list =['a','b','c','d']
# res=list(enumerate(test_list))
# print(res)


# 装饰器函数
import time


# def time_start(func):
#     def call_func():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"{(end - start):.2f}秒")
#     return call_func()

# def myfunc():
#     time.sleep(2)
#     print("time")
# myfunc = time_start(myfunc)


# 迭代函数
# def fibiter(n):
#     a=1
#     b=1
#     c=1
#     while n>2:
#         c=a+b
#         a=b
#         b=c
#         n-=1
#     return c
# print ( fibiter ( 12 ) )


# 递归函数
# def fibiter(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fibiter(n-1)+fibiter(n-2)
# print ( fibiter ( 12 ) )


# 汉诺塔
def hanoi(n, x, y, z):
    if n == 1:
        print ( x, '-->', z )
    else:
        hanoi ( n - 1, x, y, z )
        print ( x, '-->', y )
        hanoi ( n - 1, y, x, z )


n = int ( input ( '请输入汉诺塔的层数:' ) )
hanoi ( n, 'A', 'B', 'C' )

# print ( help ( hanoi ) )

print ( hanoi.__name__ )
# 以字典点的形式打印函数
print ( hanoi.__annotations__ )
# 转义文档
print ( hanoi.__doc__ )

# 是否为回文数!!!
i = '12321'
if i == i[::-1]:
    print ( '是回文数' )
else:
    print ( '不是回文数' )

# 字符串翻译练习
table = str.maketrans ( "ABCDEF", '123456' )
t = 'i love Fishic'.translate ( table )
print ( t )

print ( 'i love Fishic'.translate ( str.maketrans ( "ABCDEF", '123456' ) ) )

# 文字位置操作
x = '有内鬼,停止交易'
print ( type ( x ) )  # str
print ( x.center ( 100 ) )
print ( x.ljust ( 15 ) )
print ( x.rjust ( 15 ) )
print ( x.rjust ( 15 ) )
print ( x.zfill ( 2 ) )
print ( x.center ( 10, "淦" ) )
code = '''
  print("i love Fishic") 
    print("i love Fishic") '''
new_code = code.expandtabs ()
print ( new_code )

# 下标for循环倒序遍历
info_str = "abcde"
new_str = ""
# 从下标4开始,到下标-1结束(不包括-1),每次递减1(倒序),左闭右开区间,下标起始值为0
for i in range ( 4, -1, -1 ):
    new_str += info_str[i]
print ( new_str )

# 长度while循环倒序遍历
info_str = "abcde"
i = len ( info_str ) - 1
while i >= 0:
    print ( info_str[i], end="" )
    i -= 1
