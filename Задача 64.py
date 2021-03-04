#КОД ПРИМЕРА «Циклические алгоритмы. Обработка последовательностей и одномерных массивов»
#номер версии: 1.0
#имя файла: TA62.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Циклические алгоритмы. Обработка последовательностей и одномерных массивов
#версия Python:3.9.2
#Суммировать вводимые числа, среди которых нет нулевых. При вводе нуля обеспечить вывод текущего значения суммы. При вводе числа 99999 закончить работу.





import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
a = 0


for i in range(M):
    arr[i] = input()

for i in range(M):
    if int(arr[i]) == 99999:
        print("END")
        break
    elif int(arr[i]) == 0:
       print(a)
    elif int(arr[i]) > 0:
        a += int(arr[i])
print("Конечный результат " + str(a))
