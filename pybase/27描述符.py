class D:
    def __get__(self, instance, owner):
        return instance.x

    def __set__(self, instance, value):
        instance._x = value

    # 注意是delete函数!!!!!!
    def __delete__(self, instance):
        del instance._x


class C:
    def __init__(self, x=250):
        self._x = x

    x = D ()


c = C ()
c.x = 250
print ( c.__dict__ )
del c.x
print ( c.__dict__ )


# fget表示获取管理的相关方案,,
class MyProperty ():
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget ( instance )

    def __set__(self, instance, value):
        self.fset ( instance, value )

    def __delete__(self, instance):
        self.fdel ( instance )

    def getter(self, func):
        self.fget = func
        return self

    def setter(self, func):
        self.fset = func
        return self

    def deleter(self, func):
        # fdel你可把我害惨了!!!
        self.fdel = func
        return self


class C:
    def __init__(self):
        self._x = 250

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = MyProperty ( getx, setx, delx )


c = C ()

c.x = 500
print ( c.__dict__ )
del c.x
print ( c.__dict__ )


class D:
    def __init__(self):
        self._x = 250

    @MyProperty
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


d = D ()

d.x = 520
print ( d.__dict__ )
del d.x
print ( d.__dict__ )




# 如果实现了__set__()、__delete__()任意一个方法，那么就是数据描述符
#
# 如果只实现了__get__()方法，则为非数据描述符

class D:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print ( 'get~' )
        return instance.__dict__.get ( self.name )

    def __set__(self, instance, value):
        print ( 'set~' )
        # 中括号用于代表访问字典中的键值对!!!!!
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print ( 'delete~' )
        del instance.__dict__[self.name]


class C:
    x = D ()


c = C ()
c.x
print ( c.__dict__ )
c.x = 250
print ( c.__dict__ )
print ( c.x )
del c.x
print ( c.x )
print ( c.__dict__ )

