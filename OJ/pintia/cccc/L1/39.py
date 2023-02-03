n = int(input())
s = input()
h = []
tmp = []
for i in s:
    tmp.append(i)
    if len(tmp) == n:
        h.append(tmp)
        tmp = []
if tmp:
    h.append(tmp + [" "] * (n - len(tmp)))
h = h[::-1]
for i in range(len(h[0])):
    t = ""
    for j in range(len(h)):
        t += h[j][i]
    print(t)