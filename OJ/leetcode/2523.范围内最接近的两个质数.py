# 题目：2523.范围内最接近的两个质数
# 难度：MEDIUM
# 最后提交：2023-01-01 10:40:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

N = 10**6+10

# 对正整数n，欧拉函数是小于n的正整数中与n互质的数的数目
phi = [0] * N
phi[1] = 1
pfact = [0] * N
primes = []

# 1）莫比乌斯函数μ(n)的定义域是N；
# 2）μ(1)=1；
# 3）当n存在平方因子时，μ(n)=0；
# 4）当n是素数或奇数个不同素数之积时，μ(n)=-1；
# 5）当n是偶数个不同素数之积时，μ(n)=1。
mobious = [0] * N
mobious[1] = 1

for i in range(2, N):
    if not phi[i]:
        primes.append(i)
        phi[i] = i-1
        mobious[i] = -1
        for j in range(1, N):
            if i * j >= N:
                break
            pfact[i*j] = i
    for j in primes:
        if i * j >= N:
            break
        if i % j == 0:
            phi[i*j] = phi[i] * j
            mobious[i*j] = 0
            break
        phi[i*j] = phi[i] * (j-1)
        mobious[i*j] = mobious[i] * mobious[j]

def getfact(x):
    res = defaultdict(int)
    while x != 1:
        res[pfact[x]] += 1
        x //= pfact[x]
    return res

def factlist(x):
    res = [1]
    while x != 1:
        k = pfact[x]
        c = 0
        while x % k == 0:
            c += 1
            x //= k
        tmp = []
        for i in res:
            for j in range(1, c+1):
                tmp.append(i * pow(k, j))
        res += tmp
    return res

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        h = []
        for i in primes:
            if left <= i <= right:
                h.append(i)
        if len(h) < 2:
            return [-1, -1]
        t = 1e99
        ans = [-1, -1]
        for i in range(1, len(h)):
            if h[i] - h[i-1] < t:
                ans = [h[i-1], h[i]]
                t = h[i] - h[i-1]
        return ans