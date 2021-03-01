text = input()
print(text)
A = input("Введите системное время ПК: ")

for i in range(len(text)):
    if text[i] == ".":
        text = (text.replace(text[i], A))

print(text)




