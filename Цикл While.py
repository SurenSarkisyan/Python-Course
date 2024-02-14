# Цикл While(до тех пор пока)
# Отличие цикла while от цикла for в том что код внутри тела цикла выполняется до тех пор, пока какое-либо условие
# указанное в цикле является истинной

x = 2
while x > 1:
    print(x)
    x = x - 1

x = 5
while x < 10:
    print(x)
    x = x + 1

#x = 5
#while x < 10:
#    print(x)
#    x  += 1  # x = x +1

#x = 5
#while x < 10:
#    print(x)
#    x -= 1  # x = x - 1

x = 0
while x < 10:
    print(str(x) + " x is less than 10")
    x += 1
else:
    print(str(x) + " x now is not less than 10")
for x in range(10):
    print(str(x) + " x is less than 10")
else:
    x += 1
    print(str(x) + " x now is not less than 10")

# Использование ключевых слов в цикле while - break, continue, pass

my_list = [1, 2, 3]
for item in my_list:
    pass  # Заглушка для заполнения пустот в коде
print("Another Code")


my_list = [1, 2, 3]
for item in my_list:
    if item == 2:
        break  # break выходит из цикла по условию
    print(item)


my_list = [1, 2, 3]
for item in my_list:
    if item == 2:
        continue  # continue выведет все кроме условия то-есть 2
    print(item)












