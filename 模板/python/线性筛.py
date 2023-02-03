N = 10**6+10

# 对正整数n，欧拉函数是小于n的正整数中与n互质的数的数目
# x = d∣x ∑ φ(d)
phi = [0] * N
phi[1] = 1
pfact = [0] * N
# fact = [[] for _ in range(N)]
primes = []

# 1）莫比乌斯函数μ(n)的定义域是N；
# 2）μ(1)=1；
# 3）当n存在平方因子时，μ(n)=0；
# 4）当n是素数或奇数个不同素数之积时，μ(n)=-1；
# 5）当n是偶数个不同素数之积时，μ(n)=1。
# d∣n ∑ μ(d) = [n == 1]

# d∣n ∑ μ(d) * (n / d) = φ(n)

# g(n) = d∣n ∑ f(d) <---> f(n) = d∣n ∑ μ(d) g(n/d)
# g(n) = d∣n ∑ f(n) <---> f(n) = d∣n ∑ μ(n/d) g(n)
# mobious = [0] * N
# mobious[1] = 1

for i in range(1, N):
    if not phi[i]:
        primes.append(i)
        phi[i] = i-1
        # mobious[i] = -1
        for j in range(1, N):
            if i * j >= N:
                break
            pfact[i*j] = i
    for j in primes:
        if i * j >= N:
            break
        if i % j == 0:
            phi[i*j] = phi[i] * j
            # mobious[i*j] = 0
            break
        phi[i*j] = phi[i] * (j-1)
        # mobious[i*j] = mobious[i] * mobious[j]
    
    # for j in range(i, N, i):
    #     fact[j].append(i)

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