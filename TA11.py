#КОД ПРИМЕРА «Ветвления и оператор выбора»
#номер версии: 1.0
#имя файла: TA11.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2
#Имеется коробка со сторонами: A × B × C. Определить, пройдёт ли она в дверь с размерами M × K.


A = 5.0
B = 2.0
C = 4.0
M = 10.0
K = 3.0
S1 = 2 * C * (A + B)
S2 = M * K
if S1 <= S2:
    print("placed in the door")
else:
    print("can't fit the door")

#результат
can't fit the door
