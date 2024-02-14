# Запись в текстовый файл с его созданием

#colors_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "dark", "white"]

#with open("C:/Users/SurenSarkisyan/Desktop/Python Courses/Python Course 3/rainbow_colors.txt", "w") as rainbow_colors:  # "w" - write запись в файл
#    for color in colors_list:
#        print(color, file=rainbow_colors)


# Чтение из файла

colors_list = []
with open("C:/Users/SurenSarkisyan/Desktop/Python Courses/Python Course 3/rainbow_colors.txt", "r") as rainbow_colors:  # "r" - read
    for color in rainbow_colors:
        colors_list.append(color.strip("\n"))

print(colors_list)

# Добавление данных в уже существующий файл

with open("C:/Users/SurenSarkisyan/Desktop/Python Courses/Python Course 3/rainbow_colors.txt", "a") as rainbow_colors:  # "a" - append
    print("Grey", file=rainbow_colors)
    print("Dark Blue", file=rainbow_colors)






















