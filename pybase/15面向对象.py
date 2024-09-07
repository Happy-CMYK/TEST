
# 对象 类 实例

# 看得见摸得着的物品 客观存在

# 飞机
# 功能 飞 装载  跑
# 属性 机翼  颜色  名字
#
class Plane:
    def __init__(self):

        self.name = "测试猿号"
        self.clor = "黄黑"
        self.wings = 2

    def fly(self):
        print("飞机飞起来")

    def load(self,goods):
        print("飞机装了%s 货物" % goods)

    def run(self):
        print("飞机上跑道开始跑了")
#
#
# plane = Plane()
# print(plane.name)
# print(plane.clor)
# print(plane.wings)
# plane.load("2斤黄瓜")
# plane.run()
# plane.fly()

# 对象 功能 属性
# 创建类
# 功能就是方法 属性在__init__ 创建属性
# 实例化类 可以使用里面方法和属性

# 狗
# 功能 卖萌  吃饭 叫 跳
# 属性 颜色 名字 品种

class Dog:
    def __init__(self,name,clor,pinz):
        self.clor = clor
        self.name = name
        self.pinz = pinz

    def maimeng(self):
        print(f"{self.name}开始卖萌了")

    def chifan(self):
        print(f"{self.name}开始吃饭了")

    def shut(self):
        print(f"{self.name}开始汪汪了")


dog = Dog("大黄","黄色","金毛")
print(dog.name)
print(dog.clor)
print(dog.pinz)


dog.shut()
dog.chifan()
dog.maimeng()

dog_1 = Dog("开心","黑白","边牧")
print(dog_1.name)
print(dog_1.clor)
print(dog_1.pinz)

dog_1.shut()
dog_1.maimeng()
dog_1.chifan()

print(dog)
print(dog_1)