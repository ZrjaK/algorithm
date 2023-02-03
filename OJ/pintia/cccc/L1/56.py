h = []
for _ in range(int(input())):
    t = input().split()
    h.append((t[0], int(t[1])))
avg = sum(i[1] for i in h) / len(h) / 2
h.sort(key=lambda x: abs(x[1]-avg))
print(int(avg), h[0][0])