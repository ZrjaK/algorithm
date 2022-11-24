N = 10**6+10

# 对正整数n，欧拉函数是小于n的正整数中与n互质的数的数目
phi = [0] * N
phi[1] = 1

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
    j = 0
    for j in primes:
        if i * j >= N:
            break
        if i % j == 0:
            phi[i*j] = phi[i] * j
            mobious[i*j] = 0
            break
        phi[i*j] = phi[i] * (j-1)
        mobious[i*j] = mobious[i] * mobious[j]