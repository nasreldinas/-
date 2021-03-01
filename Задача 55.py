import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]

for i in range(M):
    arr[i] = input()

for i in range(M):
    m = 0
    for n in range(len(arr[i])):
        S = arr[i]
        if S[n] != " ":
            m += 1
        elif S[n] == " ":
            S = S[0 : m]
            print(S)