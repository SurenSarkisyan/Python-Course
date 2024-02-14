# Словари - Dict - {}
# Словари - это структуры данных которые содержат не упорядоченную последовательность различных объектов
# В словарях объекты располагаются в парах ключ:значение, доступ к значению можно получить по ключу
# Ключи это уникальный элемент по которому можно определить пару

# Пример

car_prices = {"Opel": 5000, "Toyota": 7000, "BMW": 10000}  # Dict Example
print(car_prices)
print(car_prices["Toyota"])  # Вывод цены по ключу

# Добавление элемента в словарь на последнее место

car_prices["Mazda"] = 4000
print(car_prices)

# Обновление старого значения

car_prices["Opel"] = 2000  # Обновление значения в элементе
print(car_prices)

# Удаление значения и самой переменной del

del car_prices["Toyota"]
print(car_prices)

# Удаление значения без удаления переменной

car_prices.clear()
print(car_prices)

# Пример работы

person = {
    "First Name": "Jack",
    "Last Name": "Brown",
    "Age": 43,
    "Hobbyes": ["Football", "Singing", "Photo"],
    "Children": {"Son": "Mikle","Daughter": "Pamela"}
}
print(person["Age"])
print(person["Hobbyes"])
print(person["Hobbyes"][2])  # Первый Способ получения значения из Hobbyes
print(person["Children"]["Son"])  # Первый Способ получения значения из Hobbyes

hobbies = person["Hobbyes"]  # Второй Способ получения значения из Hobbyes
print(hobbies[2])

Children = person["Children"]  # Второй Способ получения значения из Children
print(Children["Son"])

# Пример добавления новых данных в словарь

person["Car"] = "Mazda"
print(person)

# Пример изменения замены существующих данных на другие

person["Hobbyes"][0] = "Basketball"
print(person)

print(person.keys())
print(person.values())
print(person.items())  # Вывод Всех элементы в структуре кортежа
















































































