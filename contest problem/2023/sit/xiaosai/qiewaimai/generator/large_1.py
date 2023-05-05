import random

T = 10
print(T)
for _ in range(T):
    n = 10**5
    rest = random.randint(100, 1000)
    arr = [random.randint(1, 10)] * (n - rest) + [random.randint(1, 10) for _ in range(rest)]
    print(n)
    print(*arr)

