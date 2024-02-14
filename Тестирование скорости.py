# Тестирование Скорости

from time import time
from functools import wraps


# start_time = time.time()
# sum([number for number in range(100000)])
# end_time = time.time() - start_time
#
#
# start_time = time.time()
# sum(number for number in range(100000))
# end_time = time.time() - start_time

def speedtest(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f"Time of code execution {end_time- start_time}")
        return result
    return wrapper()

@speedtest
def sum_with_list():
    return sum([number for number in range(1000000)])

sum_with_list()

@speedtest
def sum_with_gen_expression():
    return sum(number for number in range(1000000))

sum_with_gen_expression()

























