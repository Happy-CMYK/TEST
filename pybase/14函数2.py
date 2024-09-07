def cla(a, b, methon="+"):
    # print(a+b)
    if methon == "+":
        return a + b
    if methon == "-":
        return a - b
    if methon == "*":
        return a * b
    if methon == "/":
        return a / b

    # print("abc")


c = cla ( 11, 22 )
print ( c )

print ( cla ( c, 44, "*" ) )

# 斐波那契函数
# def fib(n):
#     a, b = 1, 1
#     for i in range ( n - 1 ):
#         a, b = b, a + b
#     return a
#
#
# print ( fib ( 10 ) )


# # 斐波那契递归调用版本
# def fibonacci(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# n=int(input())
# print(fibonacci(n))


# 斐波那契递推版本
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         a = b = 1
#         for i in range ( 3, n + 1 ):
#             s = a + b
#             a = b
#             b = s
#         return s
# n = int ( input () )
# print ( fibonacci ( n ) )



# 统计大写,小写,数字,空格,其他字符的个数
# s = input ()
# num, Bchar, Schar, space, other = 0, 0, 0, 0, 0
# for i in s:
#     if i.isdigit ():
#         num += 1
#     elif i.isupper ():
#         Bchar += 1
#     elif i.islower ():
#         Schar += 1
#     elif i.isspace ():
#         space += 1
#     else:
#         other += 1
# print ( f'大写字母个数{Bchar}、小写字母个数: {Schar}、数字个数: {num}、空格个数: {space}、其他字符个数: {other}' )


d = "assqqqAGDJKSK"  # str
print ( type ( d ) )
num = 0  # 进入循环前需要有最初的数据
for v in d:
    if v.isupper ():
        num += 1
print ( num )


# # 冒泡排序
# # 定义需要排序的数据
data = [3, 1, 4, 2, 5]
# print(type(data))

# 使用while循环实现冒泡排序
n = len(data)
# print(n)
while n > 1:
    for i in range(n-1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
            print ( data )
    n -= 1

# 输出排序后的结果
print(data)



# list的倒叙操作
arr = [1, 2, 3, 4, 3, 4]  #list可以直接进行排序操作
re_arr = []
for i in reversed ( arr ):
    re_arr.append ( i )
print ( re_arr )
arr = [1, 2, 3, 4, 3, 4]
s = str ( arr )
print ( s )
print ( type ( s ) )
a2=arr[::-1]
print(a2)


# int的倒序操作
a = 123123
print ( type ( a ) )
a1 = str ( a )  #str类型可以进行倒序排序,此时a1="123123"
a2 = ''.join ( reversed ( a1 ) )
print ( a2 )

a2=a1[::-1]
print(a1)



def power (exp):
    def exp_of(base):
        return base ** exp
    return exp_of
square = power(2)
cube = power(3)
print ( square ( 5 ) )
print ( cube ( 5 ) )

