# Строки. Indexing & Slicing
# Индексация и вырезание частей из строк

greeting = "Hello Python!"
greeting_lenght = len(greeting)  # 1 способ вывода длинны
print(len(greeting))  # 2 способ len - длинна строки

# Вывод элемента из строки его индексация

print(greeting[0])
print(greeting[1])

# Пример получения последнего символа из строки

print(greeting[-1])

# Slicing - вырезание кусочка с подстроки или строки

print(greeting[2:5])  # Пример где мы вырезаем и 2 элемента до 5 элемента в строке
print(greeting[6:10])
print(greeting[-5:-2])
print(greeting[2:])
print(greeting[:5])
print(greeting[:])
print(greeting[::2])  # :: - обозначить шаг, двойка это шаг в данном случае перескок через одну букву
print(greeting[1::3])  # тройка так же шаг
print(greeting[1:9:3])
print(greeting[::-1])  # Трюк - любая строка наоборот




