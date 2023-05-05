import random

T = 10**2
print(T)
out = []
for _ in range(T):
    n = random.randint(1, 10**4)
    out.append(n)
print(*out, sep='\n')