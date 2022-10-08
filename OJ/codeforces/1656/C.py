from re import T


for _ in range(int(input())):
    input()
    l = [int(i) for i in input().split()]
    bad = False
    l.sort()
    for i in range(len(l)-1):
        if l[i] + 1 == l[i+1]:
            bad = True
            break
    if 1 in l and bad:
        print("NO")
    else:
        print("YES")