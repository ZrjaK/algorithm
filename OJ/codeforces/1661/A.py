for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    for i in range(1,n):
        if abs(a[i-1]-a[i])+abs(b[i-1]-b[i]) > abs(a[i-1]-b[i]) + abs(b[i-1]-a[i]):
            a[i], b[i] = b[i], a[i]
    s = 0
    for i in range(1,n):
        s += abs(a[i-1]-a[i])+abs(b[i-1]-b[i])
    print(s)