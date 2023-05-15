import random

t = 0
ans = 0
while t < 1e6:
    a = random.randint(0, 8)
    b = random.randint(0, 8)
    c = 12 - a - b
    if not 0 <= c <= 8:
        continue
    if sorted([a, b, c])[::-1] == [8, 4, 0]:
        ans += 100
    if sorted([a, b, c])[::-1] == [7, 5, 0]:
        ans += 20
    if sorted([a, b, c])[::-1] == [8, 2, 2]:
        ans += 10
    if sorted([a, b, c])[::-1] == [8, 3, 1]:
        ans += 10
    if sorted([a, b, c])[::-1] == [6, 6, 0]:
        ans += 20
    if sorted([a, b, c])[::-1] == [5, 4, 3]:
        ans += -10
    if sorted([a, b, c])[::-1] == [7, 3, 2]:
        ans += 2
    if sorted([a, b, c])[::-1] == [7, 4, 1]:
        ans += 2
    if sorted([a, b, c])[::-1] == [6, 4, 2]:
        ans += 1
    if sorted([a, b, c])[::-1] == [5, 5, 2]:
        ans += 1
    if sorted([a, b, c])[::-1] == [6, 5, 1]:
        ans += 1
    if sorted([a, b, c])[::-1] == [6, 3, 3]:
        ans += 1
    if sorted([a, b, c])[::-1] == [4, 4, 4]:
        ans += 1
    t += 1

ans /= 1e6

print(ans)