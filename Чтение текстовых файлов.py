# Чтение текстовых файлов
# input and output

# Пример

# input
#x = input("Input Somthing ")

# output
#print("Output Somthing " + x)

print(1, 2, 3, sep=":", end="\n")  # sep=":" - разделитель, end="\n" - вывод с новой строки
print(1, 2, 3, sep=",", end="\n")

# Пример помещения кода в файл

Lorem_text_file =  open("C:/Users/SurenSarkisyan/Desktop/Python Courses/Python Course 3/Sample.txt", "r")  # r - read from file
for line in Lorem_text_file:  # Чтение файла по строчно.
    print(line, end="")
Lorem_text_file.close()

# Пример перебора строк

Lorem_text_file =  open("C:/Users/SurenSarkisyan/Desktop/Python Courses/Python Course 3/Sample.txt", "r")  # r - read from file
for line in Lorem_text_file:  # Чтение файла по строчно.
    if "Mary" or "let" in line.lower():
        print(line, end="")  # Получение строк, где есть вхождение let или Mary
Lorem_text_file.close()  # Обязательно нужно закрывать файл чтобы не повредить


# with оператор для открытия текста дает возможность не закрывать файл он это делает сам

with open("C:/Users/SurenSarkisyan/Desktop/Python Courses/Python Course 3/Sample.txt", "r") as Lorem_text_file:
    for line in Lorem_text_file:  # Чтение файла по строчно.
        if "Mary" or "let" in line.lower():
            print(line, end="")  # Получение строк, где есть вхождение let или Mary


# Метод readline readlines который читает построчно из файла
# readline - читает одну строку

with open("C:/Users/SurenSarkisyan/Desktop/Python Courses/Python Course 3/Sample.txt", "r") as Lorem_text_file:
    Line = Lorem_text_file.readline()
    print(Line)
    while Line:
        print(Line, end="")
        Line = Lorem_text_file.readline()

# readlines - читает строки содержимое файла и помещает в список строки этого файла как элементы списка

with open("C:/Users/SurenSarkisyan/Desktop/Python Courses/Python Course 3/Sample.txt", "r") as Lorem_text_file:
    Line = Lorem_text_file.readlines()
print(Line, end="\n")

for Lines in Line:
    print(Lines)

# Метод read - читает весь файл и помещает его в одну строку сплошную

with open("C:/Users/SurenSarkisyan/Desktop/Python Courses/Python Course 3/Sample.txt", "r") as Lorem_text_file:
    text = Lorem_text_file.read()
print(text)




























