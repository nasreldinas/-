#КОД ПРИМЕРА «Ветвления и оператор выбора»
#номер версии: 1.0
#имя файла: TA29.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2
#Известен ГОД. Определить, будет ли этот год високосным, и к какому веку этот год относится

a = 5.0


import random

A = random.randint(1, 2018)
print("year: " + str(A))

if A % 4 == 0:
    print(str(A) + " year a leap")
elif not A % 4 == 0:
    print(str(A) + " year a not leap")

V = A // 100 + 1
print(str(A) + " year,  " + str(V) + " century ")

#результат
year: 587
587 year a not leap
587 year,  6 century 
