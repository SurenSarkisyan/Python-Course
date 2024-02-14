# Методы, Методы Класса
# Методы - это функции которые описываются или определяются внутри класса и выполняют какую-то функциональность, часто выполняют действия
# над какими-то атрибутами класса

# Пример создания метода внутри класса

class Car:

    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city):  # Пример создания метода и вызова его Opel_Car.drive()
        print(self.name + " is Drives to" + city)  # конкатенация

    def change_color(self, new_color):  # Пример метода
        self.color = new_color

Opel_Car = Car("Opel Tigra", "Grey", year="1999", is_crashed=True)
Opel_Car.drive(" London")
print(Opel_Car.wheels_number)
print(Opel_Car.name)
print(Opel_Car.color)
print(Opel_Car.year)
print(Opel_Car.is_crashed)

Mazda_Car = Car(name="Mazda CX7", color="Black", year="2014", is_crashed=False)
Mazda_Car.drive(" Paris")  # Метод drive можно использовать для конкретного объекта
Mazda_Car.change_color("Yellow")
print(Mazda_Car.color)


# Пример создания Класса и Метода внутри

class Circle:

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.circumference = 2 * self.pi * self.radius
    def get_area(self):
        return self.pi * (self.radius ** 2)

    #def get_circumference(self):  # Метод вычисления длинны окружности
    #    return 2 * self.pi * self.radius

circle_1 = Circle()
print(circle_1.get_area())
print(circle_1.circumference)
#circle_2 = Circle(3)
#print(circle_2.get_area())
#circumference = Circle()
#print(circumference.get_circumference())


# Методы уровня Класса!

class Gamer:

    active_gamers = 0  # Атрибут уровня класса, глобальная переменная

    @classmethod  #  Decorator  для создания метода уровня класса
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(",")
        return cls(nickname, age, level, points)



    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def logout(self):
        Gamer.active_gamers -= 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print("You can go to adult lrvel")
        else:
            print("You cant go to adult level")

gamer_1 = Gamer("Hell_Boy", 23, 5, 13)
gamer_2 = Gamer("Harry Potter", 13, 7,34)

print(Gamer.active_gamers)

print(gamer_1.get_age())
print(gamer_1.get_adult_level_permission())

print(gamer_2.get_age())
print(gamer_2.get_adult_level_permission())

print(Gamer.active_gamers)

gamer_1.logout()
print(Gamer.active_gamers)
print(Gamer.get_active_gamers())

James = Gamer.gamer_from_string("James,34,2,45")
Jane = Gamer.gamer_from_string("Jane,24,3,5")
print(James.get_age())
print(Jane.get_level())
print(Gamer.get_active_gamers())

my_dict = dict.fromkeys((1, 2 ,3 ), ("apple", "orange", "banana"))  # Встроеный метод dict.fromkeys
print(my_dict)


























