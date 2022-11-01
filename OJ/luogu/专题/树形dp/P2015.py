from collections import defaultdict
from functools import cache
import sys
sys.setrecursionlimit(100004)

d = defaultdict(list)
n, q = [int(i) for i in input().split()]
c = [[0] * (n+1) for _ in range(n+1)]
for _ in range(n-1):
    i, j, k = [int(i) for i in input().split()]
    d[i].append(j)
    d[j].append(i)
    c[i][j] = k
    c[j][i] = k
dp = [[0] * (q+1) for _ in range(n+1)]
@cache
def p(i, parent):
    for j in d[i]:
        if j == parent:
            continue
        p(j, i)
        for f in range(q, 0, -1):
            for k in range(f-1, -1, -1):
                dp[i][f] = max(dp[i][f], dp[j][k]+dp[i][f-k-1]+c[i][j])
p(1, -1)
print(dp[1][q])