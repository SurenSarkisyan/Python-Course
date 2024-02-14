# Вызов собственных ошибок - raise


# Пример

raise ValueError("Invalid Value")
raise ValueError()

# Пример с созданием функции

def get_rainbow_color(color_number):

    '''  # Документация для кода
    :param color_number: Color number must be integer and Color number must be in range of integer from 1 to 7
    :return:
    '''

    color_number_list = [1, 2, 3, 4, 5, 6, 7]

    if type(color_number) is not int:
        raise TypeError("Color number must be integer")
    if color_number not in color_number_list:
        raise ValueError("Color number must be in range of integer from 1 to 7")  # Отображение ошибки с использованием ключевого слова raise

    if color_number == 1:
        return "red"
    elif color_number == 2:
        return "orange"
    elif color_number == 3:
        return "yellow"
    elif color_number == 4:
        return "green"
    elif color_number == 5:
        return "blue"
    elif color_number == 6:
        return "indigo"
    elif color_number == 7:
        return "violet"

color = get_rainbow_color("Hi")
print(color)


# Пример

def color_text(color_number, text):

    color_number_list = [1, 2, 3, 4, 5, 6, 7]
    if type(color_number) is not int:
        raise TypeError("Parameter color number must be integer")
    if color_number not in color_number_list:
        raise ValueError("Parameter color number must be in range of integer from 1 to 7")  # Отображение ошибки с использованием ключевого слова raise
    if type(text) is not str:
        raise TypeError("Parameter text must be str type")

    if color_number == 1:
        print("red" + text)
    elif color_number == 2:
        print("orange" + text)
    elif color_number == 3:
        print("yellow" + text)
    elif color_number == 4:
        print("green" + text)
    elif color_number == 5:
        print("blue" + text)
    elif color_number == 6:
        print("indigo" + text)
    elif color_number == 7:
        print("violet" + text)

color_text(4," cat")
