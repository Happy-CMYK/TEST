# # 不管你输入的是什么数据,input函数都会当作字符串处理
# a = input("请输入数字:")
# b = input("请输入数字:")
#
# print("您输入的数据是:", a)
# print("您输入的数据的类型是:", type(a))
#
# print(a.isdigit())
#
# # 判断一个字符串是否是数字
# if a.isdigit():
#     print(int(a) + int(b))


# 用户输入的数据默认都是str类型(强转成int类型)
num = int(input('please input:'))
if num>0:
    print('num>0')
elif  num==0:
    print('num>0')
else:
    print('num<0')



# def add(x,y,*args):
def add(x,y,**kwargs):
    print("x的值为:", x)
    print("y的值为:", y)
    print(kwargs)

if __name__ == '__main__':
    # add("11","22")
    # add(y="11",x="22","33","122")
    # add("11","22",x="33",y="122")
    add("11","22",a="33",b="122")
    add(y="11",x="22",a="33",b="122")

