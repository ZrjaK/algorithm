from functools import lru_cache
@lru_cache(None)
def dfs(x):
    if len(x) == 1:
        return (0, int(x))
    res = (1e99, 0)
    for i in range(1, len(x)):
        a = int(x[:i])
        b = int(x[i:])
        r = dfs(str(a + b))
        res = min(res, (r[0] + 1, r[1]))
    return res

n = input()
print(*dfs(n))
