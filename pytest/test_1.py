import pytest


# 入门案例

def func(x):
    return x + 1


def test_answer():
    assert func ( 3 ) == 5


if __name__ == '__main__':
    # pytest.main ( ["-s"] )

    pytest.main ( ["-q/--quiet"] )
