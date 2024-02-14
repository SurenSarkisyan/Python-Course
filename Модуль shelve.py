# Модуль shelve - хранение данных в формате словаря при помощи формата ключ:значение, данные хранятся не в памяти, а в
# файле в отличие от модуля pickle, где данные хранятся в ячейке памяти компьютера.
# В данном методе образуется файл с расширением .db

import shelve

with shelve.open("shelve_test") as cars:
    cars["ope"] = "Germany"
    cars["ford"] = "USA"
    cars["mazda"] = "Japan"
    cars["renault"] = "France"

    print(cars["ford"])
    print(cars["renault"])
    print(cars["mazda"])
    print(cars["opel"])

    del  cars["ope"]  # Пример удаления неверного ключа из базы

    for key in cars:
        print(key)































































































