n, m, q = map(int, input().split())
r = set()
c = set()
for _ in range(q):
    t, k = map(int, input().split())
    if t == 0:
        r.add(k)
    else:
        c.add(k)
print(n * m - len(r) * m - len(c) * n + len(r) * len(c))