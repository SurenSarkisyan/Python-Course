# Обновление данных при помощи метода shelve

import shelve

monday_scedual = ["Math", "English language", "Programming", "Python"]
tuesday_scedual = ["English language", "Programming", "Python", "HTML"]
wednasday_scedual = ["Phisycs", "English language","Python"]
thursday_scedual = ["Math", "Chemistry", "Programming", "Python"]
friday_scedual = ["Math", "English language", "Programming", "Java"]
saturday_scedual = ["Math", "English language", "Running", "Programming", "Python"]


with shelve.open("scedual_file", writeback=True) as scedual:
    scedual["monday_scedual"] = monday_scedual
    scedual["tuesday_scedual"] = tuesday_scedual
    scedual["wednasday_scedual"] = wednasday_scedual
    scedual["wednasday_scedual"] = thursday_scedual
    scedual["friday_scedual"] = friday_scedual
    scedual["saturday_scedual"] = saturday_scedual


    temp_list = scedual["thursday_scedual"]  # Добавление данных через временную переменную в файл
    temp_list.append("Swimming")
    scedual["thursday_scedual"] = temp_list


    scedual["thursday_scedual"].append("Python")  # Добавление данных через временную переменную в файл


    for key in scedual:
        print(key, scedual[key])





















