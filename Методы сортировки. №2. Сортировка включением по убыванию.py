#КОД ПРИМЕРА «Методы сортировки»
#номер версии: 1.0
#имя файла: Методы сортировки. №2. Сортировка включением по убыванию.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 18.06.2021
#дата последней модификации: 18.06.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2


import random
data = [random.randint(0,10) for _ in range (20)]
for i in range(len(data)):
 j=i
 key=data[j]
 while j>0 and key > data[j-1]:
 data[j]=data[j-1]
 j=j-1
 data[j]=key
print (data)
