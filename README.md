Task-1
A = "2018-10-04"
date = A.split("-")
print(date)
print(date[2] + "/" + date[1] + "/" + date[0])

TASK2
A = 15
B = 8
C = 3
print("Max value: ", max(A, B, C))
print("Min value: ", min(A, B, C)) 

TASK3
import math 
a=5.0
b=9.0
c=7.0
P=a+b+c
p=P/2.0
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Perimeter -",P)
print("Area-",S) 

TASK4
p=250
kg=float (p)/float(1000)
t=float(p)/float(1000000)
print(kg)
print(t)

task5
a=1.0
b=1024.0
kb=(1.0/1024.0)
mb=(1.0/1024.0/1024.0)
print("kilobytes-",kb)
print("megabytes-",mb)

TASK6
X=3.0
Y=5.0
Z=(1.0/X*Y)
print("act -", Z)

TASK7
a=8.0
b=4.0
c=2.0
en=(8.0/2.0)
me=(8.0/4.0)
print("even -",en)
print("multiple -",me)

TASK8
a=5.0
b=5.0
c=2.0
en=(5.0/2.0)
me=(5.0/5.0)
print("even -",en)
print("multiple -",me)

TASK9
a=7.0
b=7.0
c=2.0
en=(7.0/2.0)
me=(7.0/7.0)
print("even -",en)
print("multiple -",me)

task10
a=10.0
b=10.0
c=2.0
en=(10.0/2.0)
me=(10.0/7.0)
print("even -",en)
print("multiple -",me)

TASK11
A=5.0
B=2.0
C=4.0
M=10.0
K=3.0
S1=2*C*(A+B)
S2=M*K
if S1<=S2:
 print ("placed in the door")
else:
 print ("can't fit the door")
 
 TASK12
 a=45.0
if a>0:
 print ("positive")
else:
 print ("negative")
if a==0:
 print("equals zeroequals zero")
 
 TASK13
 import math
D=20.0
A=12.0
if D>=A * math.sqrt(2) :
 print ("beads can be cut")
else:
 print ("beads can not be cut")
 
 TASK14
 a=5.0
b=4.0
r=15.0
k=2.0
s=a*b
if 2*r+2*k<b:
 print ("positive")
else:
 print ("negative")
 
 TASK15
 import random
X = random.randint ( 1,54)
print(X)
if X >36 :
 print("lateral")
else :
 print("coupe")
if X % 2 == 0:
 print ("top")
else:
 print ("lower")
 
 task16
 import random

M=random.randint(1,5000)
print("Money= " + str(M))

A=M%500
A1=M//500
print("500: " + str(A1))

B=A%100
B1=A//100
print("100:" + str(B1))

C=B%10
C1=B//10
print("10:" + str(C1))

D1=C//2
print("2:" + str(D1))

TASK17
import math
A=5.0
H=2.0
R=3.0
M=10
.0
CV=A**3
CYV=math.pi * R**2 * H
if CV>M:
 print ("possibly")
else:
 print ("unpossibly")
if CYV>M:
 print ("possibly")
else:
 print ("unpossibly")
if M<CYV<CV:
 print ("possibly")
else:
 print ("unpossibly")
 
 TASK18
 
 TASK19
 X=6.0
Y=5.0
Z=7.0
if X+Y>Z and X-Y<Z:
 print ("exists")
else:
 print("does not exist")
if Z**2 == X**2+Y**2:
 print ("rectangular")
else:
 print ("not rectangular")
 
 TASK20
 import random
X=random.randint (1,100)
A=0
B=20
if B>X>A:
 print ("Prinadlejit")
else:
 print("Ne prinadlejit")
 
 TASK21
 import random

x = random.randint(-100,100)
print("x = " + str(x))

y = random.randint(-100,100)
print("y = " + str(y))

z = (1.0/(x*y))
print("z = " + str(z))

TASK22
import random
A=random.randint (1,10)
B=random.randint (1,20)
C=random.randint (1,30)
if A < B < C:
 print ("performed","A < B < C")
else:
 print ("not performed","A B B>C:
 print ("performed","A > B > C")
else:
 print ("not performed","A > B > C")
 
 TASK23
 import random
import math
X= random.randint (1,15)
Y= random.randint (1,20)
print ("X -",X)
print ("Y -",Y)
if X>Y:
 Z= math.sqrt (X*Y)
 print ("Zqrt - ",Z)
else:
 Z= math.log(X+Y)
 print ("Zlog - ",Z)
 
 TASK24
 import random
A=random.randint (1.0,10.0)
B=random.randint (1.0,10.0)
C=random.randint (1.0,10.0)
D=random.randint (1.0,10.0)
S1=A*B
S2=C*D
print ("Numbers",A,B,C,D)
if S2>S1:
 print ("pomestilsya")
else:
 print ("not pomestilsya")
if A<C and B<D:
 print ("parallel")
else:
 print ("not parallel")
if A<D and B<C:
 print ("Perpendicular")
else:
 print ("not perpenicular")
 
 TASK25
 import random
X=random.randint(1,5)
if X<=2:
 f=X**2 + 4*X + 5
 print ("f("+str(X)+")="+str (f))
else:
 f= 1/(X**2 + 4*X + 5)
 print ("f("+str(X)+")="+str (f))
 
 TASK26
 import random
X=random.randint(1.0,5.0)
if X<=0:
    f=0
    print ("f("+str(X)+")="+str(f))
if 0<X<1:
    f=X
    print ("f("+str(X)+")="+str(f))
else:
    f=X**4
    print ("f("+str(X)+")="+str(f))

TASK27
import random
import math

X = random.randint(1.0, 5.)
if X<=0:
    f=0
    print ("f("+str(X)+")="+str(f))
if 0<X<1:
    f=X**2-X
    print("f(" + str(X) + ")=" + str(f))
else:
    f=X**2-math.sin(math.pi**2)
    print("f(" + str(X) + ")=" + str(f))
    
    TASK28
    A = True
B = False
if A & B or A != B:
 print("It works")
 
 TASK29
 import random
A=random.randint(0,2018)
if A%4 == 0:
 print ("leap")
else:
 print ("not leap")
b = A // 100
century = b+1
print(A)
print(century)

TASK30
A = [1,2,5,8,3,4]
maximum = A [0]
for x in A:
 if maximum < x:
  maximum = x
print (maximum)

TASK31
import random


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list


lst = init_random_list(5)
print("Исходный массив:", lst)

i = 0
while i  lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("Отсортированный массив:", lst)

TASK32
import random

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list

lst = init_random_list(9)
print("Исходный массив:", lst)
for i in range(len(lst) - 1):
    if i % 2 == 0:
        lst[i], lst[i+1] = lst[i+1], lst[i]

print("Модифицированный массив:", lst)

TASK33
import random


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list


lst = init_random_list(8)
print("Исходный массив:", lst)

val = lst[len(lst) - 1]
for i in range(len(lst)):
    val, lst[i],  = lst[i], val

print("Модифицированный массив:", lst)

TASK34
import random
import math


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list

lst = init_random_list(7)
print("Исходный массив:", lst)
centre = math.ceil(len(lst) / 2)
lst = lst[centre:] + lst[:centre]

print("Модифицированный массив:", lst)

TASK35
import random
import math

N = 11
M = 3
K = 7
P = 1

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list

lst = init_random_list(N)
print("Исходный массив:", lst)

lst[K:K+M], lst[P:P+M] = lst[P:P+M], lst[K:K+M]

print("Модифицированный массив:", lst)

TASK36
import random
import math

N = 11
M = 3
K = 5

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Исходный массив:        ", lst)

lst[K:K+M] = init_random_list(M)

print("Модифицированный массив:", lst)

TASK37
import random
import math

N = 11

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-100, 100))
        list_size = list_size - 1

    return list

lst = init_random_list(N)
print("Исходный массив:        ", lst)

sum = 0
positive_num = 0

for i in range(len(lst)):
    sum += lst[i]
    if lst[i] > 0:
        positive_num += 1
lst[0] = sum
lst[1] = positive_num
print("Модифицированный массив:", lst)

TASK38
import random
import math

N = 11
M = 3
K = 4

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-100, 100))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Исходный массив:        ", lst)

del lst[K:K+M]

print("Модифицированный массив:", lst)

TASK39
import random
import math

N = 11
M = 3
K = 4

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-1, 1))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Исходный массив:        ", lst)

i = 0
j = len(lst)
while i < j:
    if lst[i] == 0:
        del lst[i]
        j -= 1
    else:
        i += 1

print("Модифицированный массив:", lst)

TASK40
import random
import math

N = 11
M = 3
K = 4

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Исходный массив:        ", lst)

i = 0
j = len(lst)
while i < j:
    if lst[i] < 0:
        lst.insert(i+1, lst[i] * lst[i])
        j += 1

    i += 1

print("Модифицированный массив:", lst)


TASK41
import random

N = 11

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Массив:        ", lst)

is_up = True
prev = lst[0]

i = 0
while i < len(lst):
    element = lst[i]

    if element < 0:
        break

    if element < prev:
        is_up = False

    prev = element
    i += 1


if i == 0:
    print("Последовательность не успела начаться")
elif i == 1:
    print("Последовательность состоит из 1 элемента")
elif is_up:
    print("Последовательность возрастает")
else:
    print("Последовательность не возрастает")
    
    TASK42
    import random

N = 11

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Массив:        ", lst)

is_down = True
prev = lst[0]

i = 0
while i < len(lst):
    element = lst[i]

    if element  prev:
        is_down = False

    prev = element
    i += 1


if i == 0:
    print("Последовательность не успела начаться")
elif i == 1:
    print("Последовательность состоит из 1 элемента")
elif is_down:
    print("Последовательность убывает")
else:
    print("Последовательность не убывает")


TASK43
import random

N = 11

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
lst_negative = []
lst_positive = []
print("Исходный массив:        ", lst)

for element in lst:
    if element >= 0:
        lst_positive.append(element)
    else:
        lst_negative.append(element)

print("Массив с положительными элементами", lst_positive)
print("Массив с отрицательными элементами", lst_negative)


TASK44
import random

N = 11


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


def get_positive():
    return random.randint(0, 10)


def get_negative():
    return random.randint(-10, -1)


lst = init_random_list(N)
count_positive = 0
count_negative = 0

print("Исходный массив:        ", lst)

for element in lst:
    if element >= 0:
        count_positive += 1
    else:
        count_negative += 1

diff = count_positive - count_negative
need_negative = True

if diff < 0:
    need_negative = False
    diff *= -1

for i in range(0, diff):
    if need_negative:
        lst.append(get_negative())
    else:
        lst.append(get_positive())

print("Массив после модификации", lst)


TASK45
import random

N = 11


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
sum_positive = 0
sum_negative = 0

print("Исходный массив:        ", lst)

for element in lst:
    if element >= 0:
        sum_positive += element
    else:
        sum_negative += element * -1

if sum_positive > sum_negative:
    lst.append(sum_negative - sum_positive)
elif sum_positive < sum_negative:
    lst.append(sum_negative - sum_positive)

print("Сумма положительных чисел", sum_positive)
print("Модуль суммы отрицательных чисел", sum_negative)
print("Массив после модификации", lst)


TASK46
import random

N = 11
T = random.randint(0, 100)


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
count_positive = 0
print("Исходный массив:        ", lst)
print("Число T:", T)

for element in lst:
    if element >= 0:
        count_positive += 1

i = 0
while i = 0:
        lst[i] += T/count_positive

    i += 1

print("Количество положительных чисел:", count_positive)
print("Доля которая прибавляется к каждому из них:", T/count_positive)
print("Массив после модификации:", lst)


TASK47
import random

N = 11
B = -1
C = 1


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
count_positive = 0
print("Исходный массив:        ", lst)
print("Промежуток [%s, %s]:" % (B, C))

for element in lst:
    if element >= 0:
        count_positive += 1

i = 0
j = len(lst)
while i < j:
    if B <= lst[i] <= C:
        del lst[i]
        j -= 1
    else:
        i += 1

print("Массив после модификации:", lst)


TASK48
import random

N = 11


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Исходный массив:        ", lst)


i = 0
while i  1:
            lst[i] = lst[i-1] + lst[i-2]
        elif i == 1:
            lst[i] = lst[i - 1]
        else:
            print("Первый элемент 0, его нельзя заменить потому что нет предшествующих")

    i += 1

print("Массив после модификации:", lst)


TASK49
import random

N = 11


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
is_double_zero = False
print("Исходный массив:        ", lst)


i = 0
while i  0):
        if lst[i-1] == 0 and lst[i] == 0:
            is_double_zero = True
            break

    i += 1

if is_double_zero:
    print("В массиве имеются два подряд идущих нуля")
else:
    print("В массиве нет нулей идущих подряд")


TASK50
import random

N = 11


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
count_divided_by_3 = 0
sum_even = 0
count_event = 0
print("Исходный массив:        ", lst)


i = 0
while i < len(lst):
    if lst[i] % 3 == 0 and lst[i] != 0:
        count_divided_by_3 += 1

    if lst[i] % 2 == 0:
        sum_even += lst[i]
        count_event += 1

    i += 1

lst.insert(0, count_divided_by_3)
lst.append(sum_even/count_event)

print("Модифицированный массив:", lst)


TASK51
M = 2

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

max_str_len = 0

for str in list_strings:
    str_len = len(str)

    if str_len > max_str_len:
        max_str_len = str_len

print("Максимальная длина строки:", max_str_len)

for str in list_strings:
    str_len = len(str)

    if str_len < max_str_len:
        for i in range(0, max_str_len - str_len):
            str = '*' + str

    print(str)


TASK52
M = 4

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

print(' '.join(list_strings))

TASK53
import re

M = 4

def get_count(str):
    vowel = 0
    consonant = 0

    str = re.sub(r'\d', '', str)
    str = re.sub(r'\W', '', str)

    i = 0
    while i < len(str):
        char = str[i]
        if char.lower() in ['a', 'e', 'i', 'o', 'u', 'y',
                            'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']:
            vowel += 1
        else:
            consonant += 1

        i += 1

    return vowel, consonant


list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for str in list_strings:
    vowel, consonant = get_count(str)
    print("В строке %s %s гласных и %s согласных" % (str, vowel, consonant))


TASK54
import re

M = 2

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

print("Введите слог:", end=' ')
syllable = input()

for string in list_strings:
    count = len(re.findall(syllable, string))
    print("В строке \"%s\" слог \"%s\" встречается %s раз"
          % (string, syllable, count))


TASK55

import re

M = 3

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

print("Введите слог:", end=' ')
syllable = input()

for string in list_strings:
    string = re.sub(syllable, '', string)
    print(string)


TASK56
import math

M = 3

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    strlen = len(string)

    if strlen % 2 != 0:
        print(string[math.ceil(strlen/2) - 1])
        
 TASK57
 
M = 3

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    print(' '.join(string))


TASK58
from datetime import datetime

M = 3

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

now = str(datetime.now())

for string in list_strings:
    print(string.replace('.', '.' + now))


TASK59
import re

M = 3

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    count_spaces = len(re.findall(r'\s', string))
    print("В строке \"%s\" %s пробелов" % (string, count_spaces))


TASK60
import re

M = 3

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    string = re.sub(r'\?', '*', string)
    print(string)


TASK61
import re

list_numbers = []

sum = 0
sum_count = 0

multiply = 1
multiply_sum = 0


i = 1
while True:
    print("Введите число:", end=' ')
    string = re.sub(r'\D', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if i % 2 != 0:
        sum += number
        sum_count += 1
    else:
        multiply = multiply * number
        multiply_sum += 1

    i += 1
    if list_numbers[len(list_numbers) - 1] == 55555:
        break


print("Сумма:", sum)
print("Количество слагаемых:", sum_count)

print("Произведение", multiply)
print("Количество множителей:", multiply_sum)

TASK62
import re

list_numbers = []

sum = 0
sum_count = 0


i = 1
while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if i % 2 != 0:
        number *= -1
    else:
        number *= number

    sum += number
    i += 1
    if list_numbers[len(list_numbers) - 1] < 0:
        break


print("Сумма:", sum)
print("Количество слагаемых:", i)

TASK63
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

    if number 
 H:
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



TASK64
# -*- coding: utf-8 -*-
import re

list_numbers = []

sum = 0


while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number == 99999:
        break
    elif number == 0:
        print("Сумма:", sum)
    else:
        sum += number

print("Сумма:", sum)

TASK65
import re

list_numbers = []

B = 5
sum = 0

while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number < 0:
        break

    if number % B == 0:
        sum += number

print("Сумма:", sum)


TASK66
import re

list_numbers = []

count_positive = 0
count_negative = 0

while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)

    if number * -1 == 65432:
        break

    list_numbers.append(number)

    if number < 0:
        count_negative += 1
    else:
        count_positive += 1


one_percent = 100 / len(list_numbers)
print("Процент положительных чисел:", one_percent * count_positive)
print("Процент отрицательных чисел:", one_percent * count_negative)


TASK67
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
def listsum(list):
    sum = 0
    for element in list:
        sum += element

    return sum
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
tmp = list(zip(*A))
max_sum = 0
index_column_max_sum = 0
i = 0
while i  max_sum:
        max_sum = current_list_sum
        index_column_max_sum = i

    i += 1

print("Матрица:")
print_matrix(A)
print("Cтолбец для которого сумма абсолютных значений элементов максимальна:",
      index_column_max_sum)
print("Наибольший элемент этого столбца:", max(tmp[index_column_max_sum]))

TASK68
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


TASK69
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
def listsum(list):
    sum = 0
    for element in list:
        sum += element

    return sum
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
tmp = list(zip(*A))
max_sum = 0
index_column_max_sum = 0
i = 0
while i  max_sum:
        max_sum = current_list_sum
        index_column_max_sum = i

    i += 1
print("Матрица:")
print_matrix(A)
print("Cтолбец для которого сумма абсолютных значений элементов максимальна:",
      index_column_max_sum)
print("Наименьший элемент этого столбца:", min(tmp[index_column_max_sum]))

TASK70
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



TASK71
import random

N = 4 
M = 5  
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
for row in A:
    average = get_average(row)
    row.append(average)


i = 0
new_row = []
while i < len(A[0]):
    column = get_column(A, i)
    average = get_average(column)
    new_row.append(average)
    i += 1

print("Модифицированная матрица:")
A.append(new_row)

print_matrix(A)


TASK72
import random

N = 4 
M = 6  
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

sum = 0

i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        sum += A[i][j]
        j += 1

    i += 1

i = 0
new_row = []
while i < len(A):
    j = 0

    while j < len(A[i]):
        if len(new_row) <= j:
            new_row.append(A[i][j])
        else:
            new_row[j] += A[i][j]
        j += 1

    i += 1

i = 0
while i < len(new_row):
    new_row[i] = new_row[i]/sum
    i += 1

A.append(new_row)

print("Сумма всех элементов:", sum)
print("Модифицированная матрица:")
print_matrix(A)


TASK73
import random

N = 4
M = 5  
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
sum = 0
i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        sum += A[i][j]
        j += 1

    i += 1

i = 0

while i < len(A):
    j = 0

    sum_row = 0
    while j < len(A[i]):
        sum_row += A[i][j]
        j += 1

    A[i].append(sum_row/sum)

    i += 1

print("Сумма всех элементов:", sum)
print("Модифицированная матрица:")
print_matrix(A)


TASK74
import random

N = 4
M = 5 


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(-9, 9))

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
print("Исходная матрица:")
print_matrix(A)

new_row = []

i = 0
while i < len(A):
    j = 0

    count_row_negative = 0
    while j < len(A[i]):
        is_negative = A[i][j] < 0

        if is_negative:
            count_row_negative += 1

        if len(new_row) <= j:
            new_row.append(1 if is_negative else 0)
        else:
            new_row[j] += 1 if is_negative else 0

        j += 1

    A[i].append(count_row_negative)
    i += 1

A.append(new_row)

print("Модифицированная матрица:")
print_matrix(A)

TASK75
import random

N = 5  
M = 7  

L = 3
K = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(-9, 9))

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
print("Исходная матрица:")
print_matrix(A)

l_zeros = 0
k_zeros = 0


i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        if A[i][j] == 0:
            if i < L:
                l_zeros += 1

            if j < K:
                k_zeros += 1
        j += 1

    i += 1

print("В верхних %s строках содержится %s нулей" % (L, l_zeros))
print("В левых %s столбцах содержится %s нулей" % (K, k_zeros))


TASK76
import random

N = 4 
M = 5  

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



