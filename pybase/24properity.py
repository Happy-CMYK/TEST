# class C:
#     def __init__(self):
#         self.x=250
#     def getx(self):
#         return self.x
#     def setx(self,value):
#         self.x=value
#     def delx(self):
#         del self.x
#     x=property(getx,setx,delx)
#
#
# c=C()
# c.x


# _x的作用是将属性x的实现细节隐藏在类的内部.只是一种封装方式,防止外部代码直接访问和修改_x的值,从而保护了类的数据.
class C:
    def __init__(self):
        self._x = 250

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property ( getx, setx, delx )


# .x这个没有下横线的x就全权代理了_x，通过对x的访问和修改，都会影响到_x的值
c = C ()
print ( c.x )
c.x = 50
print ( c.x )
print ( c.__dict__ )
del c.x
print ( c.__dict__ )


class E:
    def __init__(self):
        self._x = 250

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


e =E()
print ( e.x )
e.x=520
print ( e.__dict__ )
del e.x
print ( e.__dict__ )