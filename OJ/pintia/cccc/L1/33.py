y, n = map(int, input().split())
x = 0
while len(set("%04d" % y)) != n:
    y += 1
    x += 1
print(x, "%04d" % y)