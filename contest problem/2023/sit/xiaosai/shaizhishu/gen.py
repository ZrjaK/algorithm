def isprime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d >>= 1
    
    for a in A:
        if a % n == 0:
            return True
        x = pow(a, d, n)
        if x != 1:
            for t in range(s):
                if x == n - 1:
                    break
                x = x * x % n
            else:
                return False
    return True

up = 9*10**8
down = 8*10**8

for i in range(up, down-1, -1):
    if isprime(i) and isprime(i + 2):
        print(i, i + 2)
        