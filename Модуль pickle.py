# Модуль pickle - дает возможность консервировать объект со всеми данными т состоянием помещать в двоичный
# файл, а затем извлекать с восстановлением данных


# Пример сохранения в двоичный файл при помощи модуля pickle

import pickle

honda = (
    "civic",
    "grey",
    "2009",
    (
        (1,"James Brown"),
        (2, "Jane White"),
        (3, "Jake Green")
    )
)

with open("honda.pickle", "wb") as honda_write:  # wb - write binary
    pickle.dump(honda, honda_write)  # pickle.dump - запись объекта honda в двоичный файл


# Пример извлечения об'єкта с использованием метода считывание

with open("honda.pickle", "rb") as honda_read:  # rb - read binary
    honda_from_file = pickle.load(honda_read)  # pickle.dump - запись объекта honda в двоичный файл
print(honda_from_file)

model, color, year, owner_list = honda_from_file

print(model)
print(color)
print(year)
for owner in owner_list:
    owner_number, owner_name = owner
    print((owner_number, owner_name))


# Пример

models = ["civic", "accord", "pilot"]
owners = ["ames Brown", "Jane White", "Jake Green"]

with open("honda.pickle", "wb") as honda_write:  # rb - write binary
    pickle.dump(honda, honda_write)  # pickle.dump - запись объекта honda в двоичный файл
    pickle.dump(models, honda_write)
    pickle.dump(owners, honda_write)
    pickle.dump(10000, honda_write)

with open("honda.pickle", "rb") as honda_read:  # rb - read binary
    honda_from_file = pickle.load(honda_read)  # pickle.dump - запись объекта honda в двоичный файл
    models = pickle.load(honda_read)
    owners = pickle.load(honda_read)
    a = pickle.load(honda_read)

print(honda_from_file)
print(models)
print(owners)
print(a)






























