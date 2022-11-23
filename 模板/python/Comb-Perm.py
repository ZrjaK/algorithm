MOD = 10**9+7
N = 10**6+10

fac = [1] * N
inv = [1] * N
for i in range(1, N):
    fac[i] = fac[i-1] * i % MOD
for i in range(2, N):
    inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD
for i in range(1, N):
    inv[i] = (inv[i-1] * inv[i]) % MOD

def C(n, m):
    return fac[n] * inv[m] * inv[n-m] % MOD if n >= m else 0
def P(n, m):
    return fac[n] * inv[n-m] % MOD if n >= m else 0