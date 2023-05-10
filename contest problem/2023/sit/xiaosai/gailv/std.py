from math import factorial

def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r)) if n >= r else 0

def P(a, b):
    return comb(8, a) * comb(8, b) * comb(8, 12 - a - b) / comb(24, 12)

ans = 0

for a in range(8 + 1):
    for b in range(min(8, 12 - a) + 1):
        c = 12 - a - b
        if 0 <= c <= 8:
            if sorted([a, b, c])[::-1] == [8, 4, 0]:
                ans += P(a, b) * 100
            if sorted([a, b, c])[::-1] == [7, 5, 0]:
                ans += P(a, b) * 20
            if sorted([a, b, c])[::-1] == [8, 2, 2]:
                ans += P(a, b) * 10
            if sorted([a, b, c])[::-1] == [8, 3, 1]:
                ans += P(a, b) * 10
            if sorted([a, b, c])[::-1] == [6, 6, 0]:
                ans += P(a, b) * 20
            if sorted([a, b, c])[::-1] == [5, 4, 3]:
                ans += P(a, b) * -10
            if sorted([a, b, c])[::-1] == [7, 3, 2]:
                ans += P(a, b) * 2
            if sorted([a, b, c])[::-1] == [7, 4, 1]:
                ans += P(a, b) * 2
            if sorted([a, b, c])[::-1] == [6, 4, 2]:
                ans += P(a, b) * 1
            if sorted([a, b, c])[::-1] == [5, 5, 2]:
                ans += P(a, b) * 1
            if sorted([a, b, c])[::-1] == [6, 5, 1]:
                ans += P(a, b) * 1
            if sorted([a, b, c])[::-1] == [6, 3, 3]:
                ans += P(a, b) * 1
            if sorted([a, b, c])[::-1] == [4, 4, 4]:
                ans += P(a, b) * 1

print(ans)
