# Объектно Ориентированное Программирование Введение в ООП Концепция Использование для описания реального объекта с
# реального мира, используются объекты и классы Класс - может быть как чертеж или рецепт или спецификация по которой
# изготавливаются все объекты этого класса, так же в классе описываются атрибуты и методы которые содержаться в
# каждом объекте класса, можно сказать что методы это функции

# Пример

help(list)
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# Пример создания собственного класса с атрибутами

class My_First_class:
    pass

object_of_my_class = My_First_class()
print(type(object_of_my_class))

# Атрибуты
# Атрибуты описывают свойства объектов из реального мира
class Car:

    wheels_number = 4  # Глобальный атрибут характерный для всех объектов класса, то-есть у всех машин 4 колеса

    def __init__(self, name, color, year, is_crashed,):  # __init__ - Метод та же функция внутри класса
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

Mazda_Car = Car(name="Mazda CX7", color="Red", year=2017, is_crashed=True)

print(Mazda_Car.name)
print(Mazda_Car.color)
print(Mazda_Car.year)
print(Mazda_Car.is_crashed)
print(Mazda_Car.wheels_number)

BMW_Car = Car(name="BMW", color="Black", year=2018, is_crashed=False)
print(BMW_Car.name)
print(BMW_Car.color)
print(BMW_Car.year)
print(BMW_Car.is_crashed)
print(BMW_Car.wheels_number)


number_of_wheels_of_3_cars = Car.wheels_number * 3  # Пример обращения к глобальному атрибуту Класса
print(number_of_wheels_of_3_cars)










































































