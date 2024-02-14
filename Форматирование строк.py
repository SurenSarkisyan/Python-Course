# Форматирование Строк

print(1 + 1)
print("1" + "1")

age= 23
print("Jack is " + str(age) + " Years old")
print("Jack is " + str(23) + " Years old")

# Пример

name = "Jack"
age = 23
name_and_age = "My name is {0}. I'am {1} years old".format(name, age)  # {0} индекс - name, {1} индекс - age
print(name_and_age)
name_and_age = "My name is {0}. I'am {1} years old".format("Jack", 23)  # format - замена параметров
print(name_and_age)

week_days = "There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}".format("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", \
                                                                            "Saturday", "Sunday")
print(week_days)

# Пример вывода по ключам

week_days = "There are 7 days in a week: {mn}, {tu}, {we}, {th}, {fr}, {st}, {sn}".format(mn="Monday", tu="Tuesday", we="Wednesday", th="Thursday", fr="Friday", \
                                                                            st="Saturday", sn="Sunday")
print(week_days)

# Пример с float

float_result = 1000 / 7
print(float_result)
print("The result of division id {0:1.3f}".format(float_result))  # {0:1.3f} - 1 колличество чисел перед точкой, 3 колличество после точки, f - float
print(""""
{0:10.2f} {1:10.2f} {2:10.2f}
{3:10.2f} {4:10.2f} {5:10.2f}
{6:10.2f} {7:10.2f} {8:10.2f}
 """.format(1.45778, 345.232352, 34.2344, 1234.23, \
                 1.45778, 345.232352, 34.2344, 1234.23, 456.666545))


# Форматирование строковых литералов f strings появился в версии 3.6 Python

name = "Jack"
age = 23
name_and_age = f"My name is {name}. I'am {age} years old."  # f - форматирование
print(name_and_age)

# Старый способы форматирования не рекомендуем для использования встречается в старом коде

name = "Jack"
age = 23
print("My name is %s. Iam %d years old" % (name, age))  # %s - string, %d - decimal

name = "Jack"
age = 23
print("My name is %s. %s %d years old" % (name, "Iam", age))




