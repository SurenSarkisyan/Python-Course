# Создание, Запись двоичных файлов и их считывание

with open("Test_binary", "bw") as test_binary:  # bw - binary write запись двоичного файла
    for number in range(21):
        test_binary.write(bytes([number]))

with open("test_binary", "br") as test_binary:  # br - binary read чтение двоичного файла
    for number in test_binary:
        print(number)










































