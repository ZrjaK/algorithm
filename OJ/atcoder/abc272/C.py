input()
a = [int(i) for i in input().split()]
a.sort()
odd = [i for i in a if i % 2]
even = [i for i in a if not i % 2]
ans = -1
if len(odd) >= 2:
    ans = max(ans, sum(odd[-2:]))
if len(even) >= 2:
    ans = max(ans, sum(even[-2:]))
print(ans)