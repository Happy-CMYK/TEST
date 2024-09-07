import pytest


# 夹具


# 模块级 (参数可选)
def setup_module(module):
    """setup any state specific to the execution of the given module."""


def teardown_module(module):
    """teardown any state that was previously setup with a setup_module
    method.
    """


# 类级 (@classmethod 可不加, 此页面没有类方法可调用)
# @classmethod
def setup_class(cls):
    """setup any state specific to the execution of the given class (which
    usually contains tests).
    """


# @classmethod
def teardown_class(cls):
    """teardown any state that was previously setup with a call to
    setup_class.
    """


# 方法级(method参数可选) (方法名称为setup 或者teardown 也可以)
def setup_method(self, method):
    """setup any state tied to the execution of the given method in a
    class.  setup_method is invoked for every test method of a class.
    """


def teardown_method(self, method):
    """teardown any state that was previously setup with a setup_method
    call.
    """


# 函数级 (function参数可选)
def setup_function(function):
    """setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """


def teardown_function(function):
    """teardown any state that was previously setup with a setup_function
    call.
    """


if __name__ == '__main__':
    # pytest.main ( ["-s", "test_3.py"] )
    pytest.main ( ["-q/--quiet"] )