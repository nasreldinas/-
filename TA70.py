#КОД ПРИМЕРА «Обработка двумерных массивов (матриц)»
#номер версии: 1.0
#имя файла: TA70.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Обработка двумерных массивов (матриц)
#версия Python:3.9.2
#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Найти наименьшее значение среди средних значений для каждой строки матрицы.


import random
import math
M = random.randint(1,5)
print("M = " + str(M))
N = random.randint(1,5)
print("N = " + str(N))
mat = [[random.randint(0,10) for y in range(M)] for i in range(N)]

for i in range(N):
    print(mat[i])

def maxaverline(mat):
   return min(sum(line) / len(line) for line in mat)
print("Ответ: " + str(maxaverline(mat)))
