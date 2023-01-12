def f(a, b, c):
    #ax+by=cを満たす最小の非負整数yを返す,存在しないなら-1
    g = gcd(a,b)
    if c == 0:
        return 0
    elif c % g != 0:
        return -1
    else:
        if g == 1:
            _, _, y = exgcd(a, b)
            return (y * c // g) % a
        else:
            return f(a//g, b//g, c//g)

def exgcd(a: int, b: int):
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = exgcd(b, a % b)
        x = q
        y = p - q * (a // b)
 
    return d, x, y