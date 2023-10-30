from math import gcd

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
        
def pollard(n):
    if n % 2 == 0:
        return 2
    if isprime(n):
        return n
    
    f = lambda x:(x * x + 1) % n
    
    step = 0
    while 1:
        step += 1
        x = step
        y = f(x)
        while 1:
            p = gcd(y - x + n, n)
            if p == 0 or p == n:
                break
            if p != 1:
                return p
            x = f(x)
            y = f(f(y))

def primefact(n):
    if n == 1:
        return []
    p = pollard(n)
    if p == n:
        return [p]
    left = primefact(p)
    right = primefact(n // p)
    return sorted(left + right)

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    PA = set(primefact(A))
    PB = set(primefact(B))
    PAB = set(primefact(A + B))
    L = len(PA & PB)
    LA = len(PA)
    LB = len(PB)
    ans = LA * LB - L + len(PAB)
    print(ans)