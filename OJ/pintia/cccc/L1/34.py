from collections import defaultdict

d = defaultdict(int)
for _ in range(int(input())):
    for i in list(map(int, input().split()))[1:]:
        d[i] += 1
ma = max(d.values())
for i in sorted(d, reverse=True):
    if d[i] == ma:
        exit(print(i, d[i]))