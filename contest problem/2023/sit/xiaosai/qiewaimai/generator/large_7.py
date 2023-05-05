import random

T = 1
print(T)
for _ in range(T):
    n = 10**6
    arr = [random.randint(1, 10) for _ in range(n)]
    print(n)
    print(*arr)

