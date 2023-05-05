h = []
while 1:
    try:
        a, _ = map(int, input().split())
        h.append(a)
    except:
        break

mx = -1
f = -1
for i in range(1, len(h)):
    if abs(h[i] - h[i-1]) > mx:
        mx = abs(h[i] - h[i-1])
        f = h[i]
print(mx, f)