# Наследование Полиморфизм ООП одна из важнейших концепций
# К примеру мы можем создать класс Грузовик в котором нам бы тоже пригодились методы drive, change_color,
# в этом случае мы можем наследоваться от класса Car то-есть создать потомок класса Car - Грузовик

class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print("Car is created")

    def drive(self, city):  # Пример создания метода и вызова его Opel_Car.drive()
        print(self.name + " is Drives to" + city)  # конкатенация

    def change_color(self, new_color):  # Пример метода
        self.color = new_color
        print("Color is changed to" + new_color)


class Truck(Car):  # Главная идея в том что когда мы создаем наследника для класса то мы можем пользоваться всеми
    # атрибутами и методами класса предка в классе наследника

    wheels_number = 6

    def __init__(self, name, color, year, is_crashed):
        Car.__init__(self, name, color, year, is_crashed)
        print("Truck is created")

    def drive(self, city):
        print("Truck " + self.name + " is Drives to" + city)

    def load_cargo(self, weight):
        print("The cargo is loaded. Weight is " + str(weight) + "kg")


MAN_truck = Truck("MAN", "White", 2015, False)

MAN_truck.drive(" New York")
print(MAN_truck.wheels_number)
MAN_truck.change_color(" Red")
MAN_truck.load_cargo(2000)

# Полиморфизм
# Методы с одинаковым названием и одинаковыми параметрами ведут себя по разному после переопределения, они разные

# Пример Полиморфизма


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Класс наследник должен имплементировать этот метод")  # Ошибка не имплементации метода


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " is saying woof")


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " is saying meow")


class Mouse(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " is saying pee-pee-pee")


class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " is saying nothing")


Spike = Dog("Spike")
Tom = Cat("Tom")
Jerry = Mouse("Jerry")
Freddy = Fish("Freddy")

pet_list = [Spike, Tom, Jerry, Freddy]

for pet in pet_list:
    pet.speak()

def pet_voice(pet):
    pet.speak()

pet_voice(Spike)
pet_voice(Tom)
pet_voice(Jerry)
pet_voice(Freddy)










