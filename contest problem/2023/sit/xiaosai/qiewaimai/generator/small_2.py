import random

T = 10**2
print(T)
for _ in range(T):
    n = 10**2
    arr = [random.randint(1, 10) for _ in range(n)]
    print(n)
    print(*arr)
