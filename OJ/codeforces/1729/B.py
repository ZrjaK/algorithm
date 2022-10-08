for _ in range(int(input())):
    input()
    s = list(input())
    ans = ""
    while s:
        t = s.pop()
        if t != "0":
            ans = chr(96+int(t)) + ans
        else:
            t = s.pop()
            t = s.pop() + t
            ans = chr(96+int(t)) + ans
    print(ans)