# Бесконечные генераторы
# Использование генераторов в бесконечном процессе

def create_patterns():
    #max_pattern_number = 100
    patterns = ("First pattern", "Second pattern", "Third pattern", "Forth pattern",
                "Fifth pattern", "Six pattern", "Seven pattern")
    i = 0
    result_list = []
    while len(result_list) < max_pattern_number:
        if i >= len(patterns):
            i = 0
        result_list.append(patterns[i])
        i += 1
    return result_list

print(create_patterns())

def get_current_pattern():
    patterns = ("First pattern", "Second pattern", "Third pattern", "Forth pattern",
                "Fifth pattern", "Six pattern", "Seven pattern")
    i = 0
    while True:
        if i >= len(patterns):
            i = 0
        yield patterns[i]
        i += 1

current_pattern = get_current_pattern()
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
















