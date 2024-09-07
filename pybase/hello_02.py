import hello_01
import pyjokes
from hello_01 import Master,cal

print(__name__)

# print(hello_01.cal(2, 2, 1))
print(cal(2, 2, 1))

class Stu(Master):
    pass

zhangsan = Stu()
zhangsan.make_cake()


joke=pyjokes.get_joke()
print(joke)