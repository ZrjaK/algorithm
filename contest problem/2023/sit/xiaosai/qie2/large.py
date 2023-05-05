import random
n = 10**4
m = 10**3
print(n, m, 10**9)
print(*([random.randint(1, 10**9) for _ in range(n)]))