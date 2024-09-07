# 这里的变量又称为属性


# 全局变量与局部变量同名
# 如果在print_str函数中没有使用global关键字显式引用全局变量，在print_str函数中将优先使用局部变量，而不是全局变量。




# 省略global关键字
# 当你的函数里只是读取全局变量的值，并没有对变量有任何的赋值行为（指a = XXX这种的写入）的话，可以省略global修饰全局变量。
first = 100  # first是全局变量
def my_hello():
    print ( first )  # 只是访问（读取）全局变量first的值，无需global修饰（加上global更规范）



# 不可省略global关键字
# 必须加上global修饰变量，说明是给全局变量name赋值，如果没有global修饰，只会说明你是在创建一个局部变量。
name = "王员外"
def change_name():
    global name
    name = "大哥大"



# 【类变量】与【实例变量】
class Person ( object ):
    TAG = "Person"  # TAG是类变量

    def __init__(self, name):  # self表示当前实例对象
        print(Person.TAG)
        # 类变量TAG被访问
        self.personName = name  # personName是实例变量

    def print_name(self):
        group = "BeiJing_"  # group是局部变量
        print ( group + self.personName )  # 局部变量 与 实例变量 拼接


if __name__ == "__main__":
    p = Person ( "WangYuanWai" )
    p.print_name ()