from collections import defaultdict
from functools import cache
import sys
sys.setrecursionlimit(100004)

d = defaultdict(list)
n, m = [int(i) for i in input().split()]
m += 1
score = [0] * (n+1)
v = set()
for x in range(1, n+1):
    k, s = [int(i) for i in input().split()]
    score[x] = s
    d[k].append(x)
dp = [[0] * (m+1) for _ in range(n+1)]
@cache
def p(i):
    dp[i][1] = score[i]
    for j in d[i]:
        p(j)
        for f in range(m, 0, -1):
            for k in range(f-1, 0, -1):
                dp[i][f] = max(dp[i][f], dp[i][f-k] + dp[j][k])
p(0)
print(dp[0][m])