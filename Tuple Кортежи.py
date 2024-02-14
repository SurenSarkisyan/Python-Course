# Кортежи - Tuple
# Есть сходство с списком но tuple - immutable
# Не изменяемая структура данных - immutable

tuple_1 = 1, 2, 3  # Можно и без скобок, но скобки нужны для определения того что это кортеж
tuple_2 = ("one", "hello")
tuple_3 = (3, 2.3, "three")

print(tuple_1)
print(type(tuple_1))
print(tuple_2)
print(tuple_3)

# Пример вывода значения по индексу

print(tuple_1[1])

# Изменение элемента

new_tuple = (tuple_1[0], 3, tuple_1[2])
print(new_tuple)

new_tuple = (tuple_1[0], 3, tuple_1[-1])  # Пример обращения по отрицательному значению
print(new_tuple)

# Пример сохранения даних целостными чтобы они были не изменяемыми в программе

x = y = z = 12  # Присвоение числа 12 каждой из переменных
x, y, z = 12, 13, 14  # Множественное присваивание в одной строке

print(x, y, z)
print(x, y, z)

person_tuple = ("john", "Smith", 1986)
first_name, last_name, year_of_birth = person_tuple
print(first_name, last_name, year_of_birth)

t1 = (1, 2, 5, 1, 7, 9)
print(t1.count(1))  # Пример сколько раз встречается 1 в кортеже

greetings_tuple = ("Hello", "Hi", "Hey", "Hi")
print(greetings_tuple.count("Hi"))

print(t1.index(5))  # Индексация пятерки в кортеже t1
print(greetings_tuple.index("Hey"))  # Индексация Hey в greetings_tuple

