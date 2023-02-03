from collections import defaultdict


n, k, s = [int(i) for i in input().split()]
h = [[int(i) for i in input().split()] for _ in range(n)]

ans = 0
d = defaultdict(int)
for a, b in h:
    if a >= 175:
        if b >= s:
            ans += 1
        else:
            if d[a] < k:
                ans += 1
                d[a] += 1
print(ans)

