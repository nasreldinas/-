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
        while j  n:
        n = average
print("Наибольшее значение среди средних значений для каждой строки "
      "матрицы:", n)
