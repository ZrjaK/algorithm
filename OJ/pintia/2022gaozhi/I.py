from functools import cache
def dfs(n, round):
    if n <= round:
        return True
    res = False
    for i in range(1, round + 1):
        res |= not dfs(n - i, round + 1)
    return res

for n in range(1, 30):
    print(n, dfs(n, 1))