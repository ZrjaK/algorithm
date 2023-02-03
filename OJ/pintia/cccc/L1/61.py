a, b = map(float, input().split())
t = a / b**2
print("%.1f" % t)
if t > 25:
    print("PANG")
else:
    print("Hai Xing")