# Условные операторы if elif else
# Условные операторы нужны, для того чтобы выполнять код на основе вычисление boolean результата, то-есть True ил False
# Веток elif может быть очень много, else всегда следует в конце если не были выполнены if или else
# Кто имеет False значения - 0, empty string, None, empty object


# Пример Условных операторов

x = 4
if x > 3:
    print("x > 3")
    print("Iam Happy!")
elif x < 3:
    print("x < 3")
else:
    print("x == 3")

# Пример использования нескольких операторов

day_time = "Night"

if day_time == "Morning":
    print("Monster Wakes up")
elif day_time == "afternoon":
    print("Monster is walk")
elif day_time == "evening":
    print("Monster is eating")
elif day_time == "Night":
    print("Monster is sleep")
else:
    print("Monster is doing somthing")

# Пример использования операторов

x = 41
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# Пример использования операторов

user_input = input("Input Somthing: ")
if user_input == "Hello!":
    print("Hello Nice to meet you")

# Пример использования операторов

if []:
    print("Somthing")

# Пример использования операторов

lucky_number = input("Enter number: ")
if lucky_number:
    print(lucky_number + " Your lucky number")  # Конкатенация результата lucky_number и строки Your lucky number
else:
    print("Enter Number")









