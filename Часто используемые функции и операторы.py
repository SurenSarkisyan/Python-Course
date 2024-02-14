# Часто используемые функции и операторы
# Ключевые слова и встроенные операторы используемые при программировании

# Range

for x in range(3, 10, 2):  # Диапазон от 3 до 10, 2 - это шаг
    print(x)
print(range(5))  #  Обьект типа range
print(list(range(5)))  #  Получение списка

#  Пример индексации строки

my_string = "adfagasg"
letter_index = 0
for letter in my_string:
    letter_index = letter_index + 1
    print(letter + " my index " + str(letter_index))

# Пример функции enumerate, где индекс связан с каждым элементом строки

my_string = "adfagasg"
for item in enumerate(my_string):
    print(item)

my_string = "adfagasg"
for index, letter in enumerate(my_string):
    print(letter + " is index " + str(index))

# Пример проверки нахождения значения в како-то последовательности

print("a" in "Jack")  # in - оператор вхождения как в Sql
print("x" in "Jack")
print(str(1) in "Jack")
print("1" in "Jack")

letter_list = ["a", "b", "c", True]
print("a" in letter_list)
print(1 in letter_list)
print(True in letter_list)

dict_1 = {1: "a", 2: "b", 3: "c"}
print(1 in dict_1)
print(1 in dict_1.keys())
print("c" in  dict_1.values())
print("z" in dict_1.values())

print(min(1, 3, 56, 4))  # min - Значение в массиве
print(max(1, 3, 43, 46))  # max - Значение в массиве

my_list = [1, 3, 45, 67]
print(min(my_list))
print(max("Hello"))  # ASCII - o имеет наибольшее значение
for letter in "Hello!":
    print(ord(letter))  # ASCII - ord функция - вывод по ASCII значениям - o имеет наибольшее значение

# Пример функций из встроенных библиотек

from random import shuffle  # random - shuffle - перемешать

my_list = [1, 3, 45, 67]
shuffle(my_list)
print(my_list)

from random import randint  # randint - random integer

print(randint(1,20))





