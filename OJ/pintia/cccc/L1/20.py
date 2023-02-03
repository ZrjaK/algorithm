n = int(input())
h = set()
for _ in range(n):
    t = list(input().split())[1:]
    if len(t) > 1:
        h |= set(t)
input()
ans = []
for i in input().split():
    if i not in h:
        ans.append(i)
        h.add(i)
if ans:
    print(*ans)
else:
    print("No one is handsome")