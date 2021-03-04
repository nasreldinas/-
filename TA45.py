#КОД ПРИМЕРА «Циклические алгоритмы. Обработка последовательностей и одномерных массивов»
#номер версии: 1.0
#имя файла: TA45.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Циклические алгоритмы. Обработка последовательностей и одномерных массивов
#версия Python:3.9.2
#Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить к элементам массива такой новый элемент, чтобы сумма элементов с положительными значениями стала бы равна модулю суммы элементов с отрицательными значениями.




import random

N = random.randint(1,10)
arr = [random.randint(-100,100) for i in range(N)]
print(arr)
sum_plus = 0
sum_minus = 0

for i in range(N):
    if arr[i] > 0:
        sum_plus += arr[i]
    elif arr[i] < 0:
        sum_minus += arr[i]

print("Sum plus number= " + str(sum_plus))
print("Sum minus number= " + str(-sum_minus))

if sum_plus > -sum_minus:
    arr.append(-(sum_minus + sum_plus))
elif sum_plus < -sum_minus:
    arr.append(-(sum_plus + sum_minus))

print(arr)
#результат

[28, -72, 56, 12, -82, 18, -35, -20]
Sum plus number= 114
Sum minus number= 209
[28, -72, 56, 12, -82, 18, -35, -20, 95]
