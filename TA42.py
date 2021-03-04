#КОД ПРИМЕРА «Циклические алгоритмы. Обработка последовательностей и одномерных массивов»
#номер версии: 1.0
#имя файла: TA42.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Циклические алгоритмы. Обработка последовательностей и одномерных массивов
#версия Python:3.9.2
Дан одномерный массив числовых значений, насчитывающий N элементов. Определить, образуют ли элементы массива, расположенные перед первым отрицательным элементом, убывающую последовательность.


import random

N = random.randint(1, 10)
arr = [random.randint(-100, 100) for i in range(N)]
print(arr)
K = 1

for i in range(0, N):
    if arr[i] < 0:
        break
    if arr[i] >= 0:
        if arr[i] > arr[i + 1] and arr[i + 1] >= 0:
            K = 1
            break
        if arr[i] < arr[i + 1]:
            K = 2

if K == 1:
    print("Not increasing sequence")
elif K == 2:
    print("Increasing sequence")
    #результат
[65, 82]
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    if arr[i] > arr[i + 1] and arr[i + 1] >= 0:
IndexError: list index out of range
