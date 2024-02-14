# Цикл for
# Возможность перебора элементов определенной последовательности

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print(str(number) + " Hola")  # Конкатенация то-есть соединение

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print("Hola!")  # Будет выведено десять раз что равно количеству элементов в переменной


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    if number % 2 == 0:  # Пример того что будут выведены четные числа
        print(number)
    else:
        print("Hi!")


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_sum = 0
for number in number_list:
    numbers_sum = numbers_sum + number
    print(numbers_sum)


greeting = "Hello Python!"
for letter in greeting:
    if letter != "o":  # Вывод слова без букв о Hell Pythn!
        print(letter)

# Пример записи без переменной

for letter in "Hello Python!":
    if letter != "o":  # Вывод слова без букв о Hell Pythn!
        print(letter)

for letter in "Hello Python!":
    print("One more letter")  # One more letter - будет выведено 13 раз что равно количеству символов в строке Hello Python!

# Пример более сложный с использованием списков в которых объекты tuple

tuple_list = [("a", "b"), ("c", "d"), ("e", "f")]
for item in tuple_list:
    print(item)
for letter_1, letter_2 in tuple_list:
    print(letter_1, letter_2)


tuple_list_1 = [("a", "b", 1), ("c", "d", 4), ("e", "f", 5)]
for letter_1, letter_2, number in tuple_list_1:
    print(letter_1, letter_2, number)

dictionary = {"Key1": "Value1", "Key2": "Value2", "Key3": "Value3"}
for item in dictionary:  # Метод обращения к ключам
    print(item)
for item in dictionary.items():  # Метод обращения и к ключам и к значениям items
    print(item)
for item in dictionary.keys():  # Метод обращения к ключам keys
    print(item)
for item in dictionary.values():  # Метод обращения к значениям values
    print(item)
for key, value in dictionary.items():  # Метод обращения и к ключам с распаковкой в переменную
    print(key)
for key, value in dictionary.items():  # Метод обращения и к значениям с распаковкой в переменную
    print(value)


# Пример использования функции range, range возвращает последовательность из чисел от нуля до указанного параметра

for x in range(5):
    print(x)

for x in range(5):
    print("Hello")  # Будет выведено 5 раз

for _ in range(5):  # _ - Underscore пример данного кода о том что не важна переменная, но важна итерация
    print(x)












