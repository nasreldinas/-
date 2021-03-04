#КОД ПРИМЕРА «Циклические алгоритмы. Обработка последовательностей и одномерных массивов»
#номер версии: 1.0
#имя файла: TA60.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 27.02.2021
#дата последней модификации: 04.03.2021
#описание: Циклические алгоритмы. Обработка последовательностей и одномерных массивов
#версия Python:3.9.2
#Заданы M строк символов, которые вводятся с клавиатуры. Каждая строка представляет собой последовательность символов, включающих в себя вопросительные знаки. Заменить в каждой строке все имеющиеся вопросительные знаки звёздочками.


text = input()
print(text)
for i in range(len(text)):
    if text[i] == "?":
        text = (text.replace(text[i], "*"))
print(text)



