from collections import defaultdict
from functools import cache
import sys
sys.setrecursionlimit(100004)

n = int(input())
d = defaultdict(list)
v = set()
for _ in range(n):
    a = [int(i) for i in input().split()]
    i = a[0]
    for j in a[2:]:
        d[i].append(j)
        v.add(j)
dp = [[0] * 2 for _ in range(n)]
@cache
def p(i):
    for j in d[i]:
        p(j)
        dp[i][0] += dp[j][1]
        dp[i][1] += min(dp[j])
    dp[i][1] += 1
for i in range(n):
    if i not in v:
        p(i)
        break
print(min(dp[i]))