import math
s = input().split()
x,y = int(s[0]), int(s[1])
r = math.sqrt(x**2+y**2)
print(x/r, y/r)