# Работа с данными модуль shelve

import shelve

with shelve.open("shelve_test") as cars:
    cars["opel"] = "Germany"
    cars["ford"] = "USA"
    cars["mazda"] = "Japan"
    cars["renault"] = "France"

    #print(cars["ford"])
    #print(cars["renault"])
    #print(cars["mazda"])
    #print(cars["opel"])

    #cars["kia"] = "Korea"

    #for key in cars:
    #    print(key + " : " + cars[key])

    #while True:
    #    key = input("Please enter car name: ")
    #    if key == "quit":
    #        break
    #    country = cars.get(key, "we dont have a " + key)
    #    print(country)

# Пример

    #while True:
    #    key = input("Please enter car name: ")
    #    if key == "quit":
    #        break
    #    if key in cars:
    #        country = cars[key]
    #        print(country)
    #    else:
    #        print("We dont have a " + key)



    #keys_list = list(cars.keys())
    #keys_list.sort()

    #for key in keys_list:
    #    print(key + " " + cars[key])

    for value in cars.values():
        print(value)
    print(type(cars.values()))

    for key in cars.keys():
        print(key)
    print(type(cars.keys()))

    for item in cars.items():
        print(item)
    print(type(cars.items()))



















