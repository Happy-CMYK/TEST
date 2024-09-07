import pytest


# 定义夹具!!

# 无返回值
@pytest.fixture ()
def before():
    print ( "before" )


# 有返回值
@pytest.fixture ()
def login():
    print ( "login" )
    return "user"


# 有参数
@pytest.fixture ()
def gen_data(request):
    print ( "gen_data" )


# 使用夹具!!

# 代码1 通常使用无返回值的夹具
@pytest.mark.usefixtures ( "before" )
def test_1():
    print ( 'test_1()' )


# 代码2 这里的用法有点怪异，但pytest做了 依赖注入处理下面的login是形参的名字，也是夹具函数的名字，pytest会调用夹具，把返回值传入此测试方法
def test_2(login):
    print ( 'test_1()', login )


# 参数化使用夹具!!

import pytest


@pytest.fixture ( params=[1, 2, 3] )
def init_data(request):
    print ( "test_data ", request.param )
    return request.param


def test_not_2(init_data):
    print ( 'test_not_2: %s' % init_data )
    try:
        assert init_data != 2
    except Exception as result:
        print ( "-" * 150 )
        print ( "捕获到了异常，信息是:%s" % result )
        print ( "-" * 150 )


if __name__ == '__main__':
    pytest.main ( ["-s", "test_4.py"] )
    pytest.main ( ["-q/--quiet"] )
