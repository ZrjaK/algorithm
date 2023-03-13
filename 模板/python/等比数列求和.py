def sum(a, n, mod):
    if n == 0:
        return 1 % mod
    if n % 2 == 0:
        return (1 + a * sum(a, n-1, mod)) % mod
    return sum(a, n // 2, mod) * (1 + pow(a, n//2+1, mod)) % mod

def calc(A, X, M):
    if A == 1:
        return(X % M)
    else:
        mod = M * (A - 1)
        x = pow(A, X, mod) - 1
        x //= (A - 1)
        return(x % M)