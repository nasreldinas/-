#КОД ПРИМЕРА «Ветвления и оператор выбора»
#номер версии: 1.0
#имя файла: TA24.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2
#Даны вещественные положительные числа a, b, c, d. Выясните, может ли прямоугольник со сторонами a,b уместиться внутри прямоугольника со сторонами c,d так, чтобы каждая сторона внутреннего прямоугольника была параллельна или перпендикулярна стороне внешнего прямоугольника.


import random

a = random.randint(1, 100)
print("a= " + str(a))

b = random.randint(1, 100)
print("b= " + str(b))

c = random.randint(1, 100)
print("c= " + str(c))

d = random.randint(1, 100)
print("d= " + str(d))

if (a <= c and b <= d) or (a <= d and b <= c):
    print("A rectangle with sides a,b can fit into a rectangle with sides c,d")

if not (a <= c and b <= d) or not (a <= d and b <= c):
    print("Rectangle with sides a,b can NOT fit into rectangle with sides c,d")
    
    #результат

a= 84
b= 8
c= 48
d= 49
Rectangle with sides a,b can NOT fit into rectangle with sides c,d
