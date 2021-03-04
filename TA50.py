#КОД ПРИМЕРА «Циклические алгоритмы. Обработка последовательностей и одномерных массивов»
#номер версии: 1.0
#имя файла: TA50.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Циклические алгоритмы. Обработка последовательностей и одномерных массивов
#версия Python:3.9.2
#Составьте блок-схему поиска максимального элемента в одномерном массиве.


import random

N = random.randint(1, 15)
arr = [random.randint(-100, 100) for i in range(N)]
print(arr)
K = 0
T = 0
t = 0
for i in range(N):
    if arr[i] % 3 == 0:
        K += 1
print("Number of multiples of three: " + str(K))

for i in range(N):
    if arr[i] % 2 == 0:
        T += arr[i]
        t += 1

A = T / t
print("Arithmetic mean: " + str(A))

arr.insert(0, K)
arr.append(A)
print(arr)

#результат
[53, -12, 55, 68, 53, 1, 31, 80, -65, -13, -1, 36, 51, -46]
Number of multiples of three: 3
Arithmetic mean: 25
[3, 53, -12, 55, 68, 53, 1, 31, 80, -65, -13, -1, 36, 51, -46, 25]
