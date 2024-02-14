# Свойства строк Методы
# Строки являются неизменяемым типом данных - immutable
# Строки в языке Python являются объектом, объекты имеют методы для работы с этими методами
# Пример среза получения нужной буквы

first_name = "Jake"
print(first_name[2])

# Пример Конкатенации

first_two_letters = first_name[:2]
print(first_two_letters)
last_letters = first_name[-1:]
print(last_letters)
Concatenable_word = first_two_letters + "n" + last_letters  # Конкатенация строк
print(Concatenable_word)

# Второй Пример Конкатенации

greeting = "Hello"
greeting = greeting + " Python!"
print(greeting)

# Пример Умножения строк

yummy = "Yum"
print(yummy * 2)

# Методы строк

yummy.upper()
print(yummy)
print(yummy.lower())

long_string = "This is long String"  # Разделитель по пробелам split
print(long_string.split())