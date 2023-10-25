n = int(input())
ans = 0
for _ in range(n):
    ans += input().count("-")
print(ans)