#КОД ПРИМЕРА «Работа с двумерными массивами (матрицами)»
#номер версии: 1.0
#имя файла: Задача № 12.py
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
A = get_matrix(N, M)
print("锐躅漤? 爨蝠桷?")
print_matrix(A)
i = 0
while i < len(A):
 j = 0
 max_element = max(A[i])
 while j < len(A[i]):
 A[i][j] /= max_element
 A[i][j] = round(A[i][j], 1)
 j += 1
 i += 1
print("填滂翳鲨痤忄眄? 爨蝠桷?")
print_matrix(A)
