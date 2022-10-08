for _ in range(int(input())):
    s = input().split()
    x = int(s[0])
    y = int(s[1])
    if x==0 and y==0:
        print(0)
    else:
        d = (x**2 + y**2) ** 0.5
        if d == int(d):
            print(1)
        else:
            print(2)