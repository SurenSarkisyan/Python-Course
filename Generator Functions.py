# Generator Functions - Генераторы єто итераторы и они могут быть созданы из функции генераторов
# yield - ключевое слово

# def my_function(x):
#     return x
#
# print(my_function(4))

# Пример создания функции генератор yield
# применение yield - дает автоматически генератор
def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count += 1

# print(count_up_to(4))
# counter = count_up_to(4)
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())

# print(next(counter))
# print(next(counter))

counter = count_up_to(10)
print(list(count_up_to(7)))

# for number in counter:
#     print(number)
counter.__next__()

for number in counter:
    print(number)

















































