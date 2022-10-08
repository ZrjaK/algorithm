for _ in range(int(input())):
    s = input()
    d = {}
    ans = 0
    a = ""
    i = 0
    for i in s:
        if a == "":
            a += i
            continue
        if i in a:
            ans += len(a) - 1
            a = ""
        else:
            a += i
    print(ans + len(a))
