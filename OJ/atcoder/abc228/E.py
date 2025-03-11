MOD = 998244353
N, K, M = [int(i) for i in input().split()]
x = pow(K, N, MOD - 1)
if not x:
    x = MOD - 1
print(pow(M, x, MOD))