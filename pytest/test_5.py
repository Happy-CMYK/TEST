import pytest


# 指定执行顺序
# 0>正数>负数
# 正数和负数一样都是值越小优先级越高


@pytest.mark.run ( order=-5)
def test_1():
    print ( "1" )


@pytest.mark.run ( order=-4 )
def test_2():
    print ( "2" )


@pytest.mark.run ( order=-3 )
def test_3():
    print ( "3" )


if __name__ == '__main__':

    pytest.main ( ["-s", "test_5.py"] )
    pytest.main ( ["-q/--quiet"] )