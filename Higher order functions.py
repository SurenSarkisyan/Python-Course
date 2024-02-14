# Higher order functions - Функции высшего порядка - те функции которые могут принимать в качестве параметров другие
# функции либо возвращать после ключевого слова return другую функцию - Декораторы

# Пример Функции высшего порядка которая принимает другую функцию как аргумент

def product(n, func):  # func - можно передать любую функцию и далее использовать, так же можно передавать встроенный в Python функции
    result = 1
    for number in range(1, n):
        result *= func(number)
    return result


def square(x):
    return x * x

print(product(3, square))

def cube(x):
    return x * x * x
print(product(3, cube))


# Пример

def my_fuction(a, b, func):
    result = func([a, b])
    return result

print(my_fuction(2, 3, sum))

# Nested function

from random import choice

def colorize(thing):
    def get_color():
        colors = ("red", "green", "yellow")
        color = choice(colors)
        return color
    result = get_color() + " "  + thing
    return result

print(colorize("apple"))


def make_color():
    def get_color():
        colors = ("red", "green", "yellow")
        color = choice(colors)
        return color
    return get_color

my_color = make_color()
print(my_color())

my_color1 = make_color()
print(my_color1())

my_color2 = make_color()
print(my_color2())

# Пример того что внутренняя функция имеет доступ к внешней

def colorize1(thing):
    def get_color():
        colors = ("red", "green", "yellow")
        color = choice(colors)
        return color + " " + thing

    return get_color

print(colorize1("apple")())
colorized1_dog = colorize1("Dog")
print(colorized1_dog())









































