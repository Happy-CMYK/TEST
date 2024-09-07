def cal(a,b,methon):
    '''
    cal函数可以有多个运算方法
    @param a:形参a表示运算方法的其中的一个数字
    @param b:形参b表示运算方法的其中的一个数字
    @param methon:形参methon表示运算方法
    @return:返回值是两个值的运算结果
    '''
    if methon == 1:
        return a + b
    if methon == 2:
        return a -b
    if methon == 3:
        return a*b
    if methon == 4:
        return a/b

    return "参数错误"

class Master(object):

    def __init__(self):
        self.old_peifang = "古法煎饼果子配方"
        self.juezhao = "边弹煎饼,边抽烟"

    def make_cake(self):
        print(f"使用古法煎饼果子配方,制作了一个煎饼果子")

    def yandan(self):
        print("抽了一个大烟袋")

    print("__name__为:",__name__)


if __name__ == '__main__':
    print(cal(1, 1, 1))

