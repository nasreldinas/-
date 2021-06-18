#КОД ПРИМЕРА «Работа с двумерными массивами (матрицами)»
#номер версии: 1.0
#имя файла: Задача № 13.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 18.06.2021
#дата последней модификации: 18.06.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2

import random
N = 4
M = 5
L = 2
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
print("锐躅漤? 爨蝠桷?")
print_matrix(A)
original_matrix = A.copy()
i = 0
while i < len(A)
