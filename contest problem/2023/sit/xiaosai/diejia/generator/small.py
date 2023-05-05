import random

n = 5
a = random.randint(1, 10)
b = random.randint(1, 10)
k1 = random.randint(1, 10)
k2 = random.randint(1, 10)
s = [random.randint(0, 1) for _ in range(n)]
print(n, a, b, k1, k1)
print("".join(map(str, s)))

m = 10
print(m)
for _ in range(m):
    print(random.randint(1, n))
