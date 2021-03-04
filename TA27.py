#КОД ПРИМЕРА «Ветвления и оператор выбора»
#номер версии: 1.0
#имя файла: TA27.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2
#Дано вещественное число A. Вычислить f(A), если f(x) = 0 при x ≤ 0; f(x) = x2 − x при 0 < x < 1, в противном случае f(x) = x2 − sin(πx2).

import random
import math

A = random.uniform(-2, 2)
print("A= " + str(A))
x = A

if x <= 0:
    print("x <= 0")
    f = 0
    print("f(A)= " + str(f))
elif 0 < x and x < 1:
    print("0 < x < 1")
    f = x ** 2
    print("f(A)= x**2 = " + str(f))
elif not x <= 0 or (0 < x and x < 1):
    print("Other case")
    pi = math.pi
    sin = math.sin(pi * x ** 2)
    f = x ** 2 - sin
    print("f(A)= " + str(f))

#результат
A= 1.37820547853
Other case
f(A)= 2.21010916256
