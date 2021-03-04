#КОД ПРИМЕРА «Циклические алгоритмы. Обработка последовательностей и одномерных массивов»
#номер версии: 1.0
#имя файла: TA44.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Циклические алгоритмы. Обработка последовательностей и одномерных массивов
#версия Python:3.9.2
#Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить столько элементов, чтобы элементов с положительными и отрицательными значениями стало бы поровну.


import random
N = random.randint(1,10)
arr = [random.randint(-100,100) for i in range(N)]
print(arr)
plus = 0
minus = 0

for i in range(N):
    if arr[i] >0:
        plus+=1
    elif arr[i] <0:
        minus+=1
if plus > minus:
    for i in range(minus , plus):
        arr.append(random.randint(-100,-1))
elif plus < minus:
    for i in range(plus , minus):
        arr.append(random.randint(1,10))

print("Nomber plus: " + str(plus))
print("Nomber minus: " + str(minus))
print(arr)

#результат
[27, -76, 49, -44, 51, -77]
Nomber plus: 3
Nomber minus: 3
[27, -76, 49, -44, 51, -77]
