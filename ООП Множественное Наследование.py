# Множественное Наследование

class Ability_swim:
    def __init__(self, name):
        print("Method init() of Ability_swim")
        self.name = name

    def greeting(self):
        print(f"Hello! My Name is {self.name} and I can swim")

    def swim(self):
        print("I am swimming")

class Ability_walk:
    def __init__(self, name):
        print("Method init() of Ability_walk")
        self.name = name

    def greeting(self):
        print(f"Hello! My Name is {self.name} and I can walk")

    def walk(self):
        print("I am walk")

class Ability_fly:
    def __init__(self, name):
        print("Method init() of Ability_fly")
        self.name = name

    def greeting(self):
        print(f"Hello! My Name is {self.name} and I can fly")

    def fly(self):
        print("I am fly")

class Game_character(Ability_swim, Ability_walk, Ability_fly):
    def __init__(self, name):
        print("Method init() of GameCharacter")
        self.name = name
        Ability_swim.__init__(self, name)
        Ability_walk.__init__(self, name)
        Ability_fly.__init__(self, name)

    #def greeting(self):
    #    print(f"Hello! My Name is {self.name}")


james = Game_character("James")
james.greeting()
james.swim()
james.walk()
james.fly()

print(isinstance(james, Ability_walk))  # isinstance - проверка является ли объект james объектом класса Ability_walk
print(isinstance(james, Ability_fly))
print(isinstance(james, Ability_swim))
print(isinstance(james, Game_character))
print(isinstance(james, object))  # object - является общим классом для всех типов данных в языке Python





























































