n = 50

a = ["n"] * n + ["w"] * n + ["i"] * n
import random
random.shuffle(a)
h = []
for i in range(0, 3 * n, 3):
    h.append("".join(a[i:i+3]))

print(n)
for i in h:
    print(i)