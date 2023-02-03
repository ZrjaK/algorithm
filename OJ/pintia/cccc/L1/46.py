x = int(input())
s = 1
while 1:
    if s % x == 0:
        print(s // x, str(s).count("1"))
        exit()
    s = s * 10 + 1