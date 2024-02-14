# Generator Expression

def get_number_from_range():
    for number in range(10):
        yield number

counter = get_number_from_range()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


# Generator Expression

counter1 = (number for number in range(10))
print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))


# Comparing generators and lists

# print(sum([number for number in range(10)]))

import time

list_start_time = time.time()
print(sum([number for number in range(100000000)]))
processing_time = time.time() - list_start_time


gen_list_start_time = time.time()
print(sum(number for number in range(100000000)))
gen_processing_time = time.time() - gen_list_start_time

print(f"Processing with {list_start_time}")
print(f"Processing with generator {gen_processing_time}")




















