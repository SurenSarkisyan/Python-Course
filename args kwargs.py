# *args  **kwargs
# args - arguments
# kwargs - key word arguments
# ** - пара означает ключ и значение, * - означает одно значение


# Пример функции которая возвращает 10% от произведения двух чисел

def ten_percent_of_product(x, y, z):  # x, y, z - позиционные параметры для присвоения
    return (x * y * z) * 0.1


print(ten_percent_of_product(10, 20, 7))


# Пример функции с использованием *args

def ten_percent_of_product_with_args(*args):  # x, y, z - позиционные параметры для присвоения и получение объекта tuple в итоге
    product = 1
    for number in args:
        product = product * number
    return product * 0.1

print(ten_percent_of_product_with_args(10, 20, 2, 1, 4, 345))


# Пример с позиционным параметром percent в начале и args - произвольная последовательность

def percent_of_product_with_args(percent, *args):  # args - произвольная последовательность параметров
    product = 1
    for number in args:
        product = product * number
    return product / 100 * percent


print(percent_of_product_with_args(10, 20, 10, 2, 1, 4, 345))


# Пример с использованием **kwargs - key word arguments

def func_with_kwargs(**kwargs):  # в key word arguments - kwargs - передаются значения в виде пар ключ=значение
    print(kwargs)

func_with_kwargs(first=1, second=2, third=3)  # Получаем вывод данных в виде словаря dict

# Пример Функции

def hello_with_kwargs(**kwargs):  # ключ должен быть словом
    if "name" in kwargs:
        print("Hello nice to meet you, {}".format(kwargs["name"]))
    else:
        print("Hello! What is you name?")

hello_with_kwargs(name="Jack", gender="male", age=24)
hello_with_kwargs(gender="male", age=24)

# Пример Функции с позиционными аргументами

def hello_with_greeting_and_kwargs(greeting, **kwargs):
    if "name" in kwargs:
        print("{}! Nice to meet you!, {}".format(greeting, kwargs["name"]))
    else:
        print("{}! what is your name?")

hello_with_greeting_and_kwargs("Good Morning!", gender="male", age=24, name="Jack")
#hello_with_greeting_and_kwargs("Hi!", gender="male", age=24)


# Пример Функции с использованием args и kwargs

def func_with_args_and_kwargs(*args, **kwargs):  # tuple for args and dict for kwargs
    print("I would like {} {}".format(args[0], kwargs["Food"]))  # args[0] - это One для kwargs ключевое слово Food

func_with_args_and_kwargs("One", "Two", name="Jack", Food="Sandwich")












