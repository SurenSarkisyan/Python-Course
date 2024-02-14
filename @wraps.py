# @wraps - Декоратор - служит, для того чтобы сохранять метаданные функции


from functools import wraps
def squares_sum(a, b):  # Сумма квадратов двух чисел
    '''
    :param a: first number
    :param b: second number
    :return: sum of squares first and second number (a*a + b*b)
    '''
    return a * a + b * b

print(squares_sum(2, 3))


def print_function_data(function):
    '''
    This is decorator function
    :param function:
    :return:
    '''
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are using {function.__name__}")
        print(f"Function Documentation {function.__doc__}")
        return function(*args, **kwargs)
    return wrapper

@print_function_data
def squares_sum(a, b):
    '''

    :param a: firs number
    :param b: second number
    :return: sum of first and second
    '''

print(squares_sum(2, 3))
print(squares_sum.__doc__)
print(squares_sum.__name__)







































