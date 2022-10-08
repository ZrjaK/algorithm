for _ in range(int(input())):
    input()
    s = input()
    count = 0
    a = ""
    for c in s:
        a += c
        if a == "((" or a == "()":
            a = ""
            count += 1
        elif len(a) > 1 and c == ")":
            a = ""
            count += 1
    print(count, len(a))