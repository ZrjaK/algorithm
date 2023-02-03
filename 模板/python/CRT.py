from functools import reduce

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def exgcd(a, b):
    if b == 0: return 1, 0
    x, y = exgcd(b, a % b)
    return y, x - a // b * y

def uni(P, Q):
    r1, m1 = P
    r2, m2 = Q

    d = gcd(m1, m2)
    assert (r2 - r1) % d == 0

    l1, l2 = exgcd(m1 // d, m2 // d)
    
    return (r1 + (r2 - r1) // d * l1 * m1) % lcm(m1, m2), lcm(m1, m2)

# x % a1 = b1  [[b1, a1]
# x % a2 = b2   [b2, a2]
# x % a3 = b3   [b3, a3]]
def CRT(eq):
    return reduce(uni, eq)