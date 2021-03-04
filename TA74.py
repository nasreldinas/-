#КОД ПРИМЕРА «Обработка двумерных массивов (матриц)»
#номер версии: 1.0
#имя файла: TA74.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Обработка двумерных массивов (матриц)
#версия Python:3.9.2
#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Определить, сколько отрицательных элементов содержится в каждом столбце и в каждой строке матрицы. Результат оформить в виде матрицы из N + 1 строк и M + 1 столбцов.


import random

N = 5
M = 7

K = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


def get_column(matrix, index):
    column = []
    i = 0
    while i < len(matrix):
        column.append(matrix[i][index])
        i += 1

    return column


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

k_column = get_column(A, K - 1)

i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        A[i][j] *= k_column[i]
        j += 1

    i += 1

print("Моифицированная матрица:")
print_matrix(A)
