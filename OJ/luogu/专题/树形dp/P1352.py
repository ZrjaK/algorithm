from collections import defaultdict
from functools import cache
import sys
sys.setrecursionlimit(100004)

n = int(input())
r = [0]
for _ in range(n):
    r.append(int(input()))
d = defaultdict(list)
v = set()
for _ in range(n-1):
    a = [int(i) for i in input().split()]
    d[a[1]].append(a[0])
    v.add(a[0])
dp = [[0] * 2 for _ in range(n+1)]
@cache
def p(i):
    for j in d[i]:
        p(j)
        dp[i][0] += max(dp[j])
        dp[i][1] += dp[j][0]
    dp[i][1] += r[i]
for i in range(1, n+1):
    if i not in v:
        p(i)
        break
print(max(dp[i]))