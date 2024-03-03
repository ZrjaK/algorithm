n, m = map(int, input().split())
t = [int(i) for i in input().split()]
t.sort()
n *= 60
ans = 0
for i in t:
    if n >= i:
        n -= i
        n -= i // 5
        ans += 1
print(ans)