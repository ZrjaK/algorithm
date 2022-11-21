N = 10**6+1
l = [1] * N
primes = []
for i in range(2, N):
    if l[i]:
        primes.append(i)
    j = 0
    for j in primes:
        if i * j >= N:
            break
        l[i*j] = 0
        if i % j == 0:
            break