# Функции
# Функция - это часть или кусок кода выполняющий функциональность

# Встроены е функции

x = print("Hello!")
y = set()

print(type(x))
print(type(y))

print(x)
print(y)

# Встроенные методы

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
my_list.clear()
print(my_list)


# Написание собственных функций

def print_greeting():  # Функция без параметра
    """
    Print "Hello!" # Описание того чо делает функция удобно для больших функций
    :return: None
    """
    print("Hello!")


# вызов функции
print_greeting()

# Получение описания функции
help(print_greeting)  # help - помогает установить что делает функция


#  Пример Функции с аргументом

def print_greeting_with_name(name=" Jack"):  # Параметр по умолчанию так же можно задать для name
    """
    :param name
    :return: None
    """
    print("Hello!" + name + "!")


print_greeting_with_name()  # Так же можно задать параметр в скобках для print_greeting_with_name
help(print_greeting_with_name)


# Функция с возвращаемым результатом

def sum_of_two_numbers(a=0, b=0):
    """
    :param a: The first parametr
    :param b: The second parametr
    :return: Sum of a and b
    """
    return a + b


x = sum_of_two_numbers(2, 5)
print(x)
help(sum_of_two_numbers)


# Пример создания функции

def is_hello_in_text(text):  # Пример функции где мы ищем вхождение слова hello в тексте
    if "hello" in text.lower():
        return True
    else:
        return False


print(is_hello_in_text("Say Hello everyone!"))


# Пример более короткий
def is_hello_in_text(text):  # Пример функции где мы ищем вхождение слова hello в тексте
    return "hello" in text.lower()


print(is_hello_in_text("Say Hello everyone!"))


# Пример функции

def is_string_in_text(string, text):
    return string in text


print(is_string_in_text("he", "The apple"))  # he содержится в The apple
print(is_string_in_text("hey", "The apple"))  # hey не содержится в The apple


# Пример функции

def greeting_depends_on_gender(name, gender):  # Данный код можно запускать в любом месте нашей программы передавая параметры
    if gender == "male":
        print("Hello!" + name + "! You look great")
        return gender                               # return - выход из функции
    elif gender == "female":
        print("Hello!" + name + "! You look perfect")
        return gender
    else:
        print("Hello!" + name + "! I never seen creature like you")
        return gender

returned_value_1 = greeting_depends_on_gender("Jack", "male")
returned_value_2 = greeting_depends_on_gender("Jane", "female")
returned_value_3 = greeting_depends_on_gender("Lo", "cmale")
print(returned_value_1)
print(returned_value_2)
print(returned_value_3)