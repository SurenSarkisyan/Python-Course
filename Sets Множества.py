# Sets - Множества {} - в отличие от dict тут располагается не пара ключ:значение, а просто уникальное значение
# Неупорядоченная коллекция уникальных элементов, то-есть в множестве не может быть двух одинаковых объектов

rainbow_colors = {"Red", "Orange", "Yellow", "Green", "Blue",
                  "Indigo", "Violet"}
print(rainbow_colors)
print(type(rainbow_colors))

# Пример создания пустого множества

empty_set = set()
print(empty_set)
print(type(empty_set))


number_list = [1, 43, 56, 1, 1, 1]
text_tuple = ("Abc", "Hello", "nice", "nice", "nice")
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)  # add - метод добавления
set_from_tuple.add("Hi")

print(set_from_list)
print(set_from_tuple)

set_from_list.pop()  # pop - метод рандомного удаления
print(set_from_list)

set_from_tuple.remove("Abc")  # Метод удаления конкретного значения remove
print(set_from_tuple)

set_from_tuple.discard("Hello")  # discard -повторно удаление удаленного ранее элемента без вывода ошибки, в отличии от remove
print(set_from_tuple)

set_from_list.clear()  # очищение множества метод clear
print(set_from_list)
