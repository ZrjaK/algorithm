n = int(input())
from functools import lru_cache
@lru_cache(None)
def calc(n):
    if n == 0:
        return 0
    return 1 + 2 * calc(n // 2)
print(calc(n))