  
#КОД ПРИМЕРА «Методы сортировки»
#номер версии: 1.0
#имя файла: Методы сортировки. №1. Сортировка включением по возрастанию.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 18.06.2021
#дата последней модификации: 18.06.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2

import random
data = [random.randint(0,10) for _ in range (20)]
for i in range(len(data)):
 j=i-1
 key= data [i]
 while data[j] > key and j >=0:
 data[j+1]= data[j]
 j-= 1
 data [j+1]=key
print (data)
