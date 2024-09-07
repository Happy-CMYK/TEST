import pytest

# mark 标记

# mark.skip 标记跳过
@pytest.mark.skip ( reason='我想跳过' )
def demo_b():
    print ( "test_b+++++" )
    return 1 / 0


# mark.xfail 标记失败
@pytest.mark.xfail ( raises=ZeroDivisionError )
def test_c():
    print ( "test_c+++++" )
    return 1 / 0



# mark.parametrize 标记参数化
@pytest.mark.parametrize ( ["a", "b"], [(1, 2), (10, 2), (111, 42), (11, 2), (12, 21)] )
def test_a(a, b):
    print ( "test_a+++++++++" )
    assert a + b > 100


if __name__ == '__main__':
    # pytest.main ( ["-s", "test_2.py"] )
    pytest.main ( ["-q/--quiet"] )
