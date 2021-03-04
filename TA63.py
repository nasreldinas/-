#КОД ПРИМЕРА «Циклические алгоритмы. Обработка последовательностей и одномерных массивов»
#номер версии: 1.0
#имя файла: TA63.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Циклические алгоритмы. Обработка последовательностей и одномерных массивов
#версия Python:3.9.2
#Даны число P и число H. Определить сумму чисел меньше P, произведение чисел больше H и количество чисел в диапазоне значений P и H. При вводе числа равного P или H, закончить работу.


import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
a = 0
b = 0
n = 0
m = 0

for i in range(M):
    arr[i] = input()

for i in range(M):
    if int(arr[0]) < 0:
        print("END")
        break
    elif i % 2 == 0:
       b += -(int(arr[i]))
       m += 1
    elif i % 2 != 0:
        a += (int(arr[i])) ** 2
        n += 1
print(" числа с нечётными номерами суммировать с обратным знаком:" + str(b))
print("количество слагаемых: " + str(m))
print("числа с чётными номерами перед суммированием возводить в квадрат: " + str(a))
print("количество сомножителей: " + str(n))




import re

P = 2
H = 10

list_numbers = []

sum = 0
multiply = 1
count = 0


while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number < P:
        sum += number
    elif number > H:
        multiply *= number

    if P < H:
        if P < number < H:
            count += 1
    else:
        if H < number < P:
            count += 1

    last_namber = list_numbers[len(list_numbers) - 1]
    if last_namber == P or last_namber == H:
        break


print("Сумма:", sum)
print("Произведение:", multiply)
print("Количество чисел в диапазоне значений P и H:", count)
