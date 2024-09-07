'''

1.元组的项是不能单独修改和删除的
2.元组的元素类型也可以不相同
3.当元组只有一个元素时,需在元素后面加上逗号,逗号至关重要,必须要写,否则就是int或str类型了
4.元组:   "*args",   或  (*args, )     逗号是最重要的,其次是小括号
5.设置元组可以写成x=()就可以,其中"()"代表元组类型的空数据
'''

# 类型
i = 123  # int

y = (123)  # int

l = "122nihao吗"  # str

a = ("122nihao吗")  # str


x = 520,  # tuple
print(type(x))

w = (520,)  # tuple

e = (520, 523)  # tuple

k = 'asjksa',  # tuple

g = ('asjksa',)  # tuple

f = ('asjksa', 'asjksa')  # tuple

j = "122", "就k123", 123  # tuple

u = ("122", "就k123", 123)  # tuple

# 创建空数据

n = int ()  # int

v = ""  # str
b = str ()  # str

m = []  # list
h = list ()  # list

t = ()  # tuple
r = tuple ()  # tuple

s = set ()  # set

z = {}  # dict
c = dict ()  # dict


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {v: k for k, v in dict1.items()}
print(dict2)  # 输出：{1: 'a', 2: 'b', 3: 'c'}
