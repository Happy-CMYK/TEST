# 1.通过定义一个计算器函数，调用函数传递三个参数,前两个参数是数据参数,最后一个参数 运算规则参数 1代表+ 2代表- 3代表* 4代表除

# def cal(a,b,methon):
#     if methon == 1:
#         return a + b
#     if methon == 2:
#         return a -b
#     if methon == 3:
#         return a*b
#     if methon == 4:
#         return a/b
#
#     return "参数错误"
#
# a = int(input("请输入要计算的值:"))
# b = int(input("请输入要计算的值:"))
# c = int(input("请输入计算规则1代表+ 2代表- 3代表* 4代表除:"))


# d = cal(a, b, c)
# print(d)



# 3.定义一个函数可以输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）返回他的BMI指数
#
# 	a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
#
# 	b.根据BMI指数，给与相应提醒
#
# 	18到24 正常 小于18 瘦 大于24 胖

# def get_bmi(h,w):
#     return w/h**2
#
# my_bmi = get_bmi(1.80,50)
# print(my_bmi)
#
# if my_bmi >24:
#     print("您太胖了需要减肥")
# elif my_bmi>18:
#     print("身材管理的真棒")
# else:
#     print("太瘦了都成麻杆了")

# h = 1.70
#
# h = input("请输入:")


# def get_bmi(h,w):
#     # h = input("请输入你的身高单位为m:")
#     # w = input("请输入你的体重单位为kg:")
#
#     h = float(h)
#     w = float(w)
#     my_bmi = w/h**2
#     if my_bmi > 24:
#         return "您太胖了需要减肥"
#     elif my_bmi>18:
#         return "身材管理的真棒"
#     else:
#         return "太瘦了都成麻杆了"
#
#
#
# # print(get_bmi(h, w))
# print(get_bmi(1.70, 80))

#
# 3.客观存在的对象(程序员),抽象成类,然后实例化 调用里面的方法和属性

class Coder:

    def __init__(self,name="张三",company="测试猿"):

        self.name = name
        self.compay = company
        print("我被调用")

    def coding(self):
        return  "%s开始写代码了" % self.name

    def fix_bug(self):
        return f"{self.name}开始修bug"

    def work_done(self,work):
        if work > 10:
            return False

        if work<=10:
            return True

# get_bmi()

coder_1= Coder()
# print(coder_1.name)
# print(coder_1.compay)
# print(coder_1.coding())
# print(coder_1.fix_bug())
#
# res = coder_1.work_done(11)
# if res:
#     print("绩效打a")
# else:
#     print("绩效打c")


#
# coder_2 = Coder("建伟","阿里巴巴")
# print(coder_2.name)
# print(coder_2.compay)
# print(coder_2.coding())
# print(coder_2.fix_bug())



