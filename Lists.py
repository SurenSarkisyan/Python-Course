# Lists, списки - Листы в Python


# Пример Добавление Элементов

number_list = [32, 21, 48, 34.56]
print(number_list)

some_list = [12, 35.334, "Hello"]
print(some_list)

some_list = [12, 35.334, "Hello"]
print(len(some_list))  #  len - колличество элементов
print(some_list[1])

another_list = some_list[:2]
print(another_list)  #  Вывод двух элементов

somes_list = [1, 2, 3, 4, 5]
somes_list[2] = "Hi"  # Добавление элемента в лист на индекс 2, либо его замена, 3 будет заменено на Hi
print(somes_list)

new_list = somes_list + another_list  # Конкатенация списков
print(new_list)

new_list.append("New Item")  # Добавление элемента в конец строки
print(new_list)

new_list.insert(0, "start")  # Вставка в начало строки, 0 - индекс метод insert
print(new_list)

# Удаление Элементов

new_list.pop()  # Удаление последнего элемента в списке
print(new_list)

new_list.pop(0)  # Удаление по индексу
print(new_list)

new_list.pop(-1)  # Удаление по индексу
print(new_list)

deleted_item = new_list.pop(-3)  # Удаление присвоение и вывод значения которое было помещено в переменную
print(deleted_item)

deleted_item = new_list.remove(12)  # Удаление по значению без возврата
print(deleted_item)


number_of_lists = [45, 12, 3, -455, 22]
letter_list = ["s", "w", "t", "a"]

number_of_lists.sort()  # sort - сортировка по алфавиту
letter_list.sort()
new_list = letter_list

print(number_of_lists)
print(letter_list)
print(new_list)

number_of_lists.reverse()  # Обратная сортировка
letter_list.reverse()
print(number_of_lists)
print(letter_list)


number_of_lists.append(letter_list)
print(number_of_lists)















