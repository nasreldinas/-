#КОД ПРИМЕРА «Работа с двумерными массивами (матрицами)»
#номер версии: 1.0
#имя файла: Задача № 15.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 18.06.2021
#дата последней модификации: 18.06.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2

from random import randint
 
number_of_colomn = int(input('Введите N: '))
number_of_row = int(input('Введите M: '))
H = int(input('Введите H: '))
my_array = []
for i in range(number_of_colomn):
    temp=[]
    for j in range(number_of_row):
        n = randint(0,10) 
        temp.append(n)
    my_array.append(temp)
print(my_array)
