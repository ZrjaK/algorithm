ns = []
ts = []
for _ in range(int(input())):
    n, t = [i for i in input().split()]
    ns.append(n)
    ts.append(t)
l = ns+ts
for n, t in zip(ns, ts):
    c = 1
    if n == t:
        c = 2
    if l.count(n) != c and l.count(t) != c:
        print("No")
        break
else:
    print("Yes")