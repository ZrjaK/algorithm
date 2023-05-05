import random

T = 10**6
print(T)
out = []
for _ in range(T):
    n = random.randint(10**5, 10**6)
    out.append(n)
print(*out, sep='\n')