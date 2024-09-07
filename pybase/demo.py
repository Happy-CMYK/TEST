from animal import Aniaml
class Dog(Aniaml):

    def eat(self):
        Aniaml.eat(self)
        # super().eat()
        print("吃完骨头摇摇头")


kaixin = Dog("开心")
print(kaixin.name)
kaixin.eat()