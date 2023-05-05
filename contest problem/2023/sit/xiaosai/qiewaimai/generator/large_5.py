import random

T = 1
print(T)
for _ in range(T):
    n = 10**6
    arr = [random.randint(1, 10**9)] * n
    print(n)
    print(*arr)

