for _ in range(int(input())):
    input()
    l = [int(i) for i in input().split()]
    if len(l) == 1:
        if l[0] == 1:
            print("YES")
        else:
            print("NO")
        continue
    ma = max(l)
    l.remove(ma)
    if ma - max(l) > 1:
        print("NO")
    else:
        print("YES")