def calc(a, b, c, d, e, f, g, h, i, j, k, l):
    x = max(0, min(d, j) - max(a, g))
    y = max(0, min(e, k) - max(b, h))
    z = max(0, min(f, l) - max(c, i))
    return x * y * z

a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())
if calc(a, b, c, d, e, f, g, h, i, j, k, l):
    print("Yes")
else:
    print("No")