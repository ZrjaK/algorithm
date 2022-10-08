for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    if y % x != 0:
        print(0, 0)
        continue
    t = y // x
    print(1, t)