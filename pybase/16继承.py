
# 老师傅 煎饼果子配方  做煎饼果子
# object 超类
from doctest import master


class Master(object):

    def __init__(self):
        self.old_peifang = "古法煎饼果子配方"
        self.juezhao = "边弹煎饼,边抽烟"


    def make_cake(self):
        print(f"使用古法煎饼果子配方,制作了一个煎饼果子")

    def yandan(self):
        print("抽了一个大烟袋")

class School:
    def __init__(self):
        self.modern_peifang = "现代煎饼果子配方"
        self.caiyi = "山东找蓝翔"

    def make_cake(self):
        print(f"使用现代煎饼果子配方,制作了一个煎饼果子")

    def play_basketball(self):
        print("打篮球,三步扣篮")

class Student(School,Master):
    def __init__(self):
        Master.__init__(self)
        # self.old_peifang = self.peifang
        School.__init__(self)
        # self.modern_peifang = self.peifang
        self.peifang = "全新的猫式煎饼果子配方"
        # 私有属性
        # self.__money = "1000000000000000000"

    def make_cake(self):
        print("使用猫式煎饼果子配方制作煎饼")

    def make_old_cake(self):
        Master.make_cake(self)

    def make_modern_cake(self):
        School.make_cake(self)

class Children(Student):
    pass

xiaomao = Children()
print(xiaomao.old_peifang)
print(xiaomao.modern_peifang)
print(xiaomao.peifang)
# print(xiaomao.__money)
xiaomao.make_cake()
xiaomao.make_old_cake()
xiaomao.make_modern_cake()

damao = Student()
# damao.__money
print(damao.peifang)
print(damao.old_peifang)
print(damao.modern_peifang)
print(damao.caiyi)
print(damao.juezhao)
damao.make_cake()
damao.make_old_cake()
damao.make_modern_cake()

# damao.yandan()
# damao.play_basketball()

# sifu = Master()
# print(sifu.peifang)
# sifu.make_cake()

# xuexiao = School()
# print(xuexiao.peifang)
# xuexiao.make_cake()


# 判断一个对象是否属于某个类或其子类的实例
print ( isinstance ( xiaomao, Student ) )

# 判断一个类是否是另一个类的子类
print ( issubclass ( Children, Student ) )
