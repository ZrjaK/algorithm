from math import gcd
a, b, c = map(int, input().split())
if gcd(a, gcd(b, c)) == 1:
    print("YES")
else:
    print("NO")