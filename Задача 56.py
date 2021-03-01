import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]

for i in range(M):
    arr[i] = input()
print(arr)

for i in range(M):
    if len(arr[i]) % 2 == 1:
        S = arr[i]
        print(S[len(arr[i]) // 2])