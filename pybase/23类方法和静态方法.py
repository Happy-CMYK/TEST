class C:
    def funA(self):
        print ( self )

    @classmethod
    def funB(cls):
        print ( cls )


c = C ()
c.funA ()

c.funB ()


class C:
    count = 0

    def __init__(self):
        C.count += 1

    @classmethod
    def get_count(cls):
        print ( f"该类一共实例化了{cls.count}个对象" )


c1 = C ()
c2 = C ()
c3 = C ()

c1.get_count ()


class C:
    count = 0

    @classmethod
    def add(cls):
        cls.count += 1

    def __init__(self):
        self.add ()

    @classmethod
    def get_count(cls):
        print ( f"该类一共实例化了{cls.count}个对象" )


class D ( C ):
    count = 0


class E ( C ):
    count = 0

c1 = C ()
d1, d2 = D (), D ()
e1, e2, e3 = E (), E (), E ()
c1.get_count ()
d1.get_count ()
e1.get_count ()



# 导入日历模块
import calendar


# 创建一个日历类
class Time_Test ( object ):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    # 请看，这个静态函数压根就和该类没有直接的交互，只是寄存在了该类的命名空间中
    @staticmethod
    def show_claendar(year, monther):
        # 调用该模块下的配件month获取某年某月日历，并存储在变量中
        cal = calendar.month ( year, monther )
        # 将变量返回
        return cal


# 使用类名.静态方法名来调用输出静态方法
print ( Time_Test.show_claendar ( 2020, 8 ) )
# 实例化对象
time = Time_Test ( 20, 57, 30 )
# 使用实例对象去调用并输出静态方法
print ( time.show_claendar ( 2020, 7 ) )

