# Специальный (магические) методы - __Method_name__
# Все встроенные методы, которые начинаются с двух подчеркиваний

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def __str__(self):
        return self.first_name + " " + self.last_name

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.age + other.age

    def __del__(self):  # Деструктор объекта, всегда когда удаляет из памяти сборщик мусора, если обьект одинок он
        # удаляется
        print("Person object with naame " + self.first_name + "is deleted from memory")


Jack = Person("Jack", "White", 45)
Jane = Person("Jane", "Eyre", 23)

print(Jack + Jane)


print([1, 2, 3, 4, 5, 6, 7, 8])
print(Jack)
print(len(Jack))
#del (Jack)
#print(Jack)


# Пример логики сложения разных типов значений, и то как методы реализованы для разных типов данных

x = 5
y = 3

a = "5"
b = "3"

print(x.__add__(y))
print(a.__add__(b))
















