s = input().split()
n, k, x = int(s[0]), int(s[1]), int(s[2])
l = [int(i) for i in input().split()]
for i in range(len(l)):
    if k < 0:
        break
    k -= l[i] // x
    l[i] %= x
l.sort(reverse=True)
if k < 0:
    print(sum(l)-k*x)
else:
    for i in range(len(l)):
        if k == 0:
            break
        l[i] = 0
        k -= 1
    print(sum(l))