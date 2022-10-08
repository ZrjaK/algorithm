for _ in range(int(input())):
    s = input().split()
    target = int(s[1])
    l = [int(i) for i in input().split()]
    ls = set(l)
    for i in l:
        if i + target in ls:
            print("YES")
            break
    else:
        print("NO")