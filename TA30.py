#КОД ПРИМЕРА «Циклические алгоритмы. Обработка последовательностей и одномерных массивов»
#номер версии: 1.0
#имя файла: TA30.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Циклические алгоритмы. Обработка последовательностей и одномерных массивов
#версия Python:3.9.2
#Составьте блок-схему поиска максимального элемента в одномерном массиве.

A = [1, 2, 5, 8, 3, 4]
maximum = A[0]
for x in A:
    if maximum < x:
        maximum = x
print(maximum)

#результат
8
