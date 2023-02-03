a = list(map(int, input().split()))
n = int(input())
t = a[:]
 
for i in range(6):
    if a[i] < 6:
        a[i] = 6
    else:
        a[i] -= 1
for z in range(n - 1):
    for i in range(6):
        a[i] -= 1
        if a[i] == t[i]:
            a[i] -= 1
        if a[i] < 1:
            a[i] = 1
print(*a)