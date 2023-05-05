import random

T = 1
print(T)
for _ in range(T):
    n = 10**6
    arr = [random.randint(10**9-10, 10**9) for _ in range(n)]
    print(n)
    print(*arr)

