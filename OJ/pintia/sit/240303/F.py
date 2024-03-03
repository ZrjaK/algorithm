n, m, k = map(int, input().split())
S = [input() for _ in range(n)]
from itertools import permutations
m -= 1
k -= 1
ans = []
for lst in permutations(S):
    if lst[m] == "aye" and lst[k] == "AYE":
        ans.append(lst)
print(len(ans))
ans.sort()
for i in ans:
    print(*i)