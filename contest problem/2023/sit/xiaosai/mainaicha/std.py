N = 10**6 + 10
fact = [0] * N
for i in range(1, N):
    for j in range(i, N, i):
        fact[j] += 1

for i in range(1, N):
    fact[i] += fact[i-1]

T = int(input())
out = []

for _ in range(T):
    n = int(input())
    out.append(fact[n])

print(*out, sep='\n')
