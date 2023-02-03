n, m = map(int, input().split())
for _ in range(m):
    s = input()
    t = 0
    for i in s:
        if i == "y":
            t = 2 * t
        else:
            t = 2 * t + 1
    print(t + 1)