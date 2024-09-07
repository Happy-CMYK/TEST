# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# # 模余
# # 模除
# # 取余数
# print(a%b)
# # 整除
# print(a#b)


# 运算符 只能在数字之间运算
# 但是 有些运算 在str之间有特殊的作用
# a = "abc"
# b = "zhangsan"
# +字符串的拼接
# print(a+b)
# name="张三"
# age = "10"
# print("我叫"+name+"我今年"+age+"岁")


# a =10
# a = a+1
# 简写成
# a+=1
# print(a)
# # 取余数
# print(a%b)
# # 整除
# print(a#b)


# 运算符 只能在数字之间运算
# 但是 有些运算 在str之间有特殊的作用
# a = "abc"
# b = "zhangsan"
# +字符串的拼接
# print(a+b)
# name="张三"
# age = "10"
# print("我叫"+name+"我今年"+age+"岁")
# print("*"*20)
# print("*"*20)


# 成员运算(返回布尔值)
# list=[1,2,3,4,5]
# print(1 in list)
# print(1 not in list)


# 通过ASCII的值获取对应的字符
# print(chr(97))

# 通过字符获取对应的ASCII码
# print(ord("a"))

# 正序：在原有列表的基础上排序,没有返回值
# list=[4,2,33,51]
# list.sort()

# 倒序:
list = [4, 2, 33, 51]
list.sort ( reverse=True )

print ( list[:] )

list.copy ()
print ( list.copy () )

# 打印倒叙列表
list.reverse ()
print ( list )

# sorted():会生成新的列表
list = [4, 2, 33, 51]
list_2 = sorted ( list )  # 正序
list_3 = sorted ( list, reverse=True )  # 倒序

# 打印2的个数
print ( list.count ( 2 ) )







# 运算符的多态
print ( 3 + 5 )  # 结果为8
print ( 'L' + 'ove' )  # 结果为Love

# 函数的多态
print ( len ( 'Love' ) )  # 结果为4
print ( len ( ['lala', 'jiji', 'xixi'] ) )  # 结果为3
