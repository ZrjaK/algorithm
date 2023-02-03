a, b = map(int, input().split())
fa = fb = 0
for i in map(int, input().split()):
    if i == 0:
        fa += 1
    else:
        fb += 1
if fa + a > fb + b and fa:
    print(f"The winner is a: {a} + {fa}")
else:
    print(f"The winner is b: {b} + {fb}")