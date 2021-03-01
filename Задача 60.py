text = input()
print(text)

for i in range(len(text)):
    if text[i] == "?":
        text = (text.replace(text[i], "*"))

print(text)

