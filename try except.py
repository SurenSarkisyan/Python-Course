# try except
# Срабатывает только тот блок except в котором совершена ошибка

print("Some Code")
try:
    print(len(23))
    print(my_variable)
except NameError:
    print("Name Error has happened")
except TypeError:
    print("Type Error has happened")
print("Code After Error")


# Пример с использованием функции

user_dictionary = {"first_name": "Jack", "Last_name": "White", "Age": 24}

# print(user_dictionary["Last_name"])
# print(user_dictionary["name"])  # keyError

# print(user_dictionary.get("Last_name"))
# print(user_dictionary.get("name"))

def get_dict_value(dictionary, key):

    '''
    if dictionary hasn't specified key function returns None
    :param dictionary:
    :param key:
    :return:
    '''

    try:
        return dictionary[key]
    except KeyError:
        return None

print(get_dict_value(user_dictionary, "Age"))
print(get_dict_value(user_dictionary, "a"))
print(get_dict_value(user_dictionary, "first_name"))





































































