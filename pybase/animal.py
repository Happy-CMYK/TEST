
class Aniaml:
    # init 是初始化
    """

    """
    def __init__(self,name,age=0):
        self.name =name
        self.age = age
        self.type = "狗"

    def eat(self):
        print("狗吃骨头")

if __name__ == '__main__':
    aa = Aniaml("旺旺")
    print(aa.name)
    print(aa.type)
    aa.eat()