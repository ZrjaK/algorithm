n, m, k = map(int, input().split())
ans = [n, m]
for i in range(1, k):
    t = ans[i] * ans[i-1]
    for i in str(t):
        ans.append(int(i))
print(*ans[:k])