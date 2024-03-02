class Animal:
    def __init__(self, name):
        self.name = name
        # def make_sound(self):
        #     return  "unknown"

class dog(Animal):
    def make_sound(self):
        return  "woof"

class Cat(Animal):
    def make_Sound(self):
        return  "Meow"

luna = Cat("luna")
print(luna.name, luna.make_Sound())

rex = dog("Rex")
print(rex.name, rex.make_sound())
