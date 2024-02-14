# Строки - Strings

# Пример работы с переменной

greeting = "Hello"
first_name = "Jack"
last_name = "White"
exclamation_sign = "!"
white_space = " "
print(greeting + white_space + first_name + white_space + last_name + exclamation_sign)

# Пример работы с переменной

long_string = "This is the long string"
print(long_string)

whole_sentence = greeting + first_name + last_name + exclamation_sign \
+ white_space  # \ - символ переноса на новую строку из языка програмирования С
print(whole_sentence)

# Escaping \ - Пример использования одинарных и двойных кавычек и бекслеша

some_string = 'I\'m proggramer'  # \ - игнор кавычки перед буквой m
print(some_string)

some_string = "I'm proggramer"
print(some_string)

another_string = 'I want to learn "Python"'
print(another_string)

# Пример перехода на новую строку

string_with_new_line = "Hello \n My name is John"  # \n - начало с новой строки
print(string_with_new_line)

string_with_new_line = "Hello \n    \rMy name is John"  # \r - удаляет все пробелы и автоматически возвращяет в начало
# строки
print(string_with_new_line)

numbers = "1\t234567"  # \t - tab - табуляция
print(numbers)

some_text = "\tHello! \n\tI'am glad to see you"
print(some_text)

# Triple quotes - Тройные кавычки - игнорирует какие-либо кавычки внутри
# ''' Hello ''' а так-же """ Hello """ - удобно для написания больших текстов

string_with_triple_quotes = """This is text with "Triple quotes" """
another_string_with_triple_quotes = '''This is text with 'Triple quotes' '''
print(string_with_triple_quotes)
print(another_string_with_triple_quotes)



