n, a = input().split()
n = int(n)
ans = a * n
for _ in range((n+1)//2):
    print(ans)