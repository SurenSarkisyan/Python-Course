# Вложенные Списки

nested_list = [[1, 2, 3,], [4, 5, 6,], [7, 8, 9], [10, 11, 12, 13]]
print(nested_list)
print(len(nested_list))   # Длинна списка
print(len(nested_list[1])) # Длинна второго элемента
print(len(nested_list[-1]))  # Длинна последнего
print(nested_list[1][1])  # Элемент во втором списке равный 5

# Get number 12
print(nested_list[-1][2]) # Вывод числа 12
print(nested_list[3][2])  # Вывод числа 12
print(nested_list[-1][-2])  # Вывод числа 12

# Print nested_list

nested_list = [[1, 2, 3,], [4, 5, 6, True], [7, 8, 9, "Text"], [10, 11, 12, 13], [False, "Hello"]]

for inner_list in nested_list:
    print(inner_list)

for inner_list in nested_list:
    for number in inner_list:
        print(number)

# Comprehension
[[print(number) for number in inner_list] for inner_list in nested_list]