# Переменные
# Python имеет динамическую типизацию данных

x = 5
print(x)

x = "Hello"
print(x)

x = 7.9
type_of_variable = x
print(type(type_of_variable))

# Пример того как нужно давать названия переменным

car_color = "Black"  # SnakeCase - нижнее подчеркивание, основной стандарт
carColor = "Yello"  # Camel Case - Не номинален для использования
# car-color = "Blue"  # Kebab Case - не используется в Python

# Пример работы с переменными

x = 10
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x ** y)
print(x % y)

# Пример работы с переменной

credit = 1000
credit_rate = 10
number_of_years = 5
final_sum = credit + credit / 100 * credit_rate * number_of_years

print(final_sum)