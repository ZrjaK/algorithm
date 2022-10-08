from collections import defaultdict


n, m = [int(i) for i in input().split()]
d = defaultdict(set)
for p in range(m):
    a = [int(i) for i in input().split()]
    for i in a[1:]:
        d[i].add(p)
def check():
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if len(d[i] & d[j]) == 0:
                return False
    return True
if check():
    print("Yes")
else:
    print("No")
