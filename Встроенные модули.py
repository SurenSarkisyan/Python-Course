# Встроенные Модули в языке Python
# Можно сказать что модуль это файл с Python кодом, который можно использовать в дальнейшем например функцию
# Рассмотрим встроенные модули - это те модули которые установлены в языке по умолчанию

# Пример

import random  # random модуль
x = random.randint(1, 10)  # randint - модуль
print(x)


from random import randint  # Пример импорта модуля randint из основного пакета модулей random
x = random.randint(1, 10)  # randint - модуль
print(x)

from random import shuffle  # Пример импорта модуля shuffle из основного пакета модулей random
my_list = [1, 2, 3]
shuffle(my_list)
print(my_list)


from random import shuffle as shuffle_my_list  # Пример импорта модуля shuffle под присвоенным именем shuffle_my_list
# из основного пакета модулей random
my_list = [1, 2, 3]
shuffle_my_list(my_list)
print(my_list)

















































