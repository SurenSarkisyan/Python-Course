# Dictionary and Set Comprehension

# Пример # Dictionary Comprehension

number_dict = {"first": 1, "second": 2, "third": 3}
new_dict = {key: value ** 3 for key, value in number_dict.items()}
print(new_dict)


number_list = [6, 43, -2, 11, -55, -12, 3, 345]
number_dict = {number: number ** 2 for number in number_list}
print(number_dict)


number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
number_dict = {number: "Positive" if number > 0 else "Negative" if number < 0 else "Zero" for number in number_list}
print(number_dict)

# Set Comprehension

number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
number_set = {number ** 2 for number in number_list}
print(number_set)


number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
number_set = {number ** 2 for number in range(3, 11)}  # использование чисел в диапазоне от 3 до 11
print(number_set)


letter_set = {letter.upper() for letter in "Hello"}  # Уникальные не повторяющиеся значения
print(letter_set)





