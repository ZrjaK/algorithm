for _ in range(int(input())):
    s = input()
    n1 = s[0]
    n2 = s[1]
    res = (ord(n1)-ord('a'))*25+ord(n2)-ord('a')+1
    if ord(n2)>ord(n1):
        res -= 1
    print(res)