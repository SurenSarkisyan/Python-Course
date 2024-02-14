# # Iterable & Iterator - Перебирать элементы последовательности
# # Iterable - объект элемента которого можно перебрать (списки, словари, строки)
#
# number_list = [1, 2, 3, 4, 5]
#
# for number in number_list:
#     print(number)
#
# for letter in "my_string":  # Iterables объект - my_string
#     print(letter)
#
# # Пример Iterator - переборщик можно получить с использованием метода iter
#
# number_list_iterator = iter(number_list)
# print(type(number_list_iterator))
#
# string_iterator = iter("my string")
# print(type(string_iterator))
#
# # Метод next для Iterator (iter)
#
# # print(number_list_iterator.__next__())  # Последовательный переход к элементам
# # print(number_list_iterator.__next__())
# #
# #
# # print(string_iterator.__next__())
# # print(string_iterator.__next__())
#
# print(next(number_list_iterator))
# print(next(number_list_iterator))

# Пример

def my_for_loop(iterable):
    iterator = iter(iterable)
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(next(iterator))

    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print("Iteration finish")
            break

my_for_loop("Hello")
my_for_loop([1, 2, 3, 4, 5])








