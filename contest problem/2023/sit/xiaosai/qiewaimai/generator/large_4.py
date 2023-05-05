import random

T = 10**5
print(T)
for _ in range(T):
    n = 10
    arr = [random.randint(10**9-10, 10**9) for _ in range(n)]
    print(n)
    print(*arr)

