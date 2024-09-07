# __contains__(self, item)
class C:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):

        print ( "检测到 in or not in 操作！" )
        return item in self.data  # 检索item是否存在


c = C ( [1, 2, 3, 4, 5] )  # 向实例对象中输入一个列表
print ( 3 in c )


# 检测到 in or not in 操作！
# True


# 代偿  # 当没找到contains函数时,会调用iter和next函数
class C:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        print ( "iter", end='->' )
        self.i = 0
        return self  # 返回迭代器

    def __next__(self):
        print ( "next", end='->' )
        if self.i == len ( self.data ):  # 等到下标值与对应数据长度相等时，结束寻找
            raise StopIteration
        item = self.data[self.i]
        self.i += 1
        return item


c = C ( [1, 2, 3, 4, 5] )
print ( 3 in c )
# iter->next->next->next->True
print ( 6 in c )


# iter->next->next->next->next->next->next->False


# 布尔测试
class D:
    def __bool__(self):
        print ( "boy jiji boy~" )
        return True  # 默认一直返回Ture


d = D ()
bool ( d )


# boy jiji boy~
# True


# 如果找不到__bool__ ()，Python会去寻找__len__ () 这个魔法方法。
class D:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        print ( "len" )
        return len ( self.data )


d = D ( "Python" )
bool ( d )

# len
# True





# 比较运算
# 这些方法主要作用于：人们一般都会认为比较字符串比较的是字符串的长度，而不是比较每个字符串的编码值大小，但事实不是这样，结果是恰恰相反的
class S ( str ):
    def __lt__(self, other):
        return len ( self ) < len ( other )

    def __gt__(self, other):
        return len ( self ) > len ( other )

    def __eq__(self, other):
        return len ( self ) == len ( other )


s1 = S ( "Python" )
s2 = S ( "python" )
# 下面比较的不是编码值的大小，而是比较的字符串长度
print ( s1 < s2 )
# False
print ( s1 > s2 )
# False
print ( s1 == s2 )
# True
print ( s1 != s2 )


# True


# 比较字符串的功能__lt__# __le__# __gt__# __ge__# __eq__

# 将比较字符串的功能更改为比较字符串的长度
class S ( str ):
    def __lt__(self, other):
        return len ( self ) < len ( other )

    def __gt__(self, other):
        return len ( self ) > len ( other )

    def __eq__(self, other):
        return len ( self ) == len ( other )

    def __ne__(self, other):
        return len ( self ) != len ( other )

    # __ne__ = None #若不想让某个魔法方法生效，可以直接将其赋值为None


s1 = S ( "Python" )
s2 = S ( "python" )

print ( s1 != s2 )
'''
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s1!=s2
TypeError: 'NoneType' object is not callable
'''
