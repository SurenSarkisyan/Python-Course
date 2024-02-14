# else finally

# if we have error - except block work and else block doesn't work
# if we have't error - except block doesn't work and else block work
# finally block - выполняется в любом случае

# while True:
#
#     try:
#         number = int(input("Enter Some Number: "))
#         print(number / 2)
#     except:
#         print("You have to enter a number")
#     else:
#         print("Good Job! this is a number")
#         break
#     finally:
#         print("Finally block")
#
# print("Code After Error handling")


# Пример

def devide(x, y):
    try:
        print(x / y)
    except ZeroDivisionError as Error:
        print("You can't divide by zero! ")
        print(Error)
    except TypeError as E:
        print("x and y must be numbers")
        print(E)
    else:
        print("x was diveded by y")
    finally:
        print("Finally block")


print(devide(4, 2))
print(devide(4, 0))
print(devide(4, "Hi"))
























