# 题目：2514.统计同位异构字符串数目
# 难度：HARD
# 最后提交：2022-12-25 00:09:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

MOD = 10**9+7
N = 10**5+10

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

class Solution:
    def countAnagrams(self, s: str) -> int:
        h = s.split(" ")
        ans = 1
        for i in h:
            t = P(len(i), len(i))
            c = Counter(i)
            for j in c:
                t *= pow(P(c[j], c[j]), -1, MOD)
            ans *= t
            ans %= MOD
        return ans