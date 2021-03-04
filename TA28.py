#КОД ПРИМЕРА «Ветвления и оператор выбора»
#номер версии: 1.0
#имя файла: TA28.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2
#Составить алгоритм и программу для реализации логических операций «И» и «ИЛИ» для двух переменных.


import random

time = ("morning", "noon", "evening",  "night")
TIME = random.choice(time)
print("Time: " + str(TIME))

season = ("autumn" , "winter" , "spring" , "summer")
SEASON = random.choice(season)
print ("Season: " + str(SEASON) + '\n')

print("WEATHER FORECAST:" + '\n')

if (TIME == "night" and SEASON == "autumn") or (TIME == "night" and SEASON == "winter") or (TIME == "night" and SEASON == "spring") or (TIME == "evening" and SEASON == "winter"):
    print("It's very cold outside!!!")

elif (TIME == "noon" and SEASON == "winter") or (TIME == "morning" and SEASON == "winter") or (TIME == "evening" and SEASON == "autumn") or (TIME == "noon" and SEASON == "autumn") or (TIME == "morning" and SEASON == "autumn") or (TIME == "evening" and SEASON == "spring") or (TIME == "noon" and SEASON == "spring") or (TIME == "morning" and SEASON == "spring"):
    print("It's not too cold outside!!!")

elif (TIME == "night" and SEASON == "summer") or (TIME == "evening" and SEASON == "summer") or (TIME == "noon" and SEASON == "summer") or (TIME == "morning" and SEASON == "summer"):
    print("It's warm outside!!!")
    
    
    #результат
Time: evening
Season: winter

WEATHER FORECAST:

It's very cold outside!!!
