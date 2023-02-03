a, b, c = map(float, input().split())
if b == 0:
    a *= 2.455
else:
    a *= 1.26
print("%.2f" % a, ["T_T", "^_^"][a < c])