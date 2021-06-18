import random

N = 2  # строк
M = 3  # столбцов

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
def get_average(row):
    sum = 0
    for element in row:
        sum += element

    return sum/len(row)
A = get_matrix(N, M)
print("Матрица:")
print_matrix(A)
n = False
for row in A:
    average = get_average(row)
    if n is False or average < n:
        n = average
print("Наименьшее значение среди средних значений для каждой строки "
      "матрицы:", n)
