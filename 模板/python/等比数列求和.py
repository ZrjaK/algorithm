def sum(a, n, mod):
    if n == 0:
        return 1
    if n % 2 == 0:
        return (1 + a * sum(a, n-1, mod)) % mod
    return sum(a, n // 2, mod) * (1 + pow(a, n//2+1, mod)) % mod