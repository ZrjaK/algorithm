from typing import Counter

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = Counter(l)
    a = c.most_common(1)[0][1]
    res = 0
    while a < n:
        res += 1
        res += a
        a *= 2
    res -= a-n
    print(res)