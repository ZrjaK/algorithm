def inv(a, p):
    _, x, _ = exgcd(a, p)
    return x % p

# x % a1 = b1
# x % a2 = b2
# x % a3 = b3
# ...
# a1,a2,a3互质
def CRT(a, b):
    p = reduce(mul, a)
    x = 0
    for i in range(len(a)):
        r = p // a[i]
        x += (b[i] * r * inv(r, a[i])) % p
    return x % p