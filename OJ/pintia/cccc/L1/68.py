n = int(input())
s = 0
for i in map(float, input().split()):
    s += 1 / i
print("%.2f" % (1 / (s / n)))