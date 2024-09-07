import pytest
import random

# 失败重试  -5


def test_num():


    num = random.randint ( 1, 10 )

    assert num > 8

if __name__ == '__main__':

    pytest.main ( ["-q/--quiet"] )
    pytest.main ( ['-s', '--reruns', '5', 'test_6.py'] )
