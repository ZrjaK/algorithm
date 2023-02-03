for _ in range(int(input())):
    t = input().split()
    x = float(t[1])
    if t[0] == "M":
        print("%.2f" % (x / 1.09))
    else:
        print("%.2f" % (x * 1.09))