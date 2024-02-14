# Конвертация словаря в объект shelve

# Создание Словаря

# university = {
# "Sceduals": {
#     "monday_scedual": ["Math", "English language", "Programming", "Python"],
#     "tuesday_scedual": ["English language", "Programming", "Python", "HTML"],
#     "wednasday_scedual": ["Phisycs", "English language","Python"],
#     "thursday_scedual": ["Math", "Chemistry", "Programming", "Python"],
#     "friday_scedual": ["Math", "English language", "Programming", "Java"],
#     "saturday_scedual": ["Math", "English language", "Running", "Programming", "Python"]
#     },
#
# "Teachers":{
#     "Math": ["Jack White", "Jim Black"],
#     "Python": ["Me", "Jane Smith"]
#     }
# }
#
# print(university["Sceduals"]["wednasday_scedual"])
# print(university["Teachers"]["Math"])


# Пример конвертации в метод shelve

import shelve

university = shelve.open("university_file")
university["Sceduals"] = {
    "monday_scedual": ["Math", "English language", "Programming", "Python"],
    "tuesday_scedual": ["English language", "Programming", "Python", "HTML"],
    "wednasday_scedual": ["Phisycs", "English language","Python"],
    "thursday_scedual": ["Math", "Chemistry", "Programming", "Python"],
    "friday_scedual": ["Math", "English language", "Programming", "Java"],
    "saturday_scedual": ["Math", "English language", "Running", "Programming", "Python"]
    }

university["Teachers"] = {
    "Math": ["Jack White", "Jim Black"],
    "Python": ["Me", "Jane Smith"]
    }

# x = university["Sceduals"]
# print(type(x))

print(university["Sceduals"]["wednasday_scedual"])
print(university["Teachers"]["Math"])

university.close()

























































