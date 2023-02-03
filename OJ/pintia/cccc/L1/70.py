h = []
while 1:
    s = input()
    if s == ".":
        break
    h.append(s)
print(len(h))
t1 = -1
t2 = 0
for i in range(len(h)):
    if "chi1 huo3 guo1" in h[i]:
        if t1 == -1:
            t1 = i + 1
        t2 += 1
if t2:
    print(t1, t2)
else:
    print("-_-#")