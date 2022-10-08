from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)
n, m, k = [int(i) for i in input().split()]
@lru_cache(None)
def p(index,rest):
    if index == n:
        if rest < 0:
            return 0
        else:
            return 1
    res = 0
    for i in range(1,m+1):
        res += p(index+1,rest-i)%998244353
    return res
res = p(0, k)
print(res%998244353)