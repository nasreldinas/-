#КОД ПРИМЕРА «Ветвления и оператор выбора»
#номер версии: 1.0
#имя файла: TA15.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2
#Дан номер места в плацкартном вагоне. Определить, какое это место: верхнее или нижнее, в купе или боковое.

import random

X = random.randint(1, 54)
print(X)
if X > 36:
    print("lateral")
else:
    print("coupe")
if X % 2 == 0:
    print("top")
else:
    print("lower")

    #результат
    52
lateral
top
