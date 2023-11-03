cur = 2
ans = 0
for i in range(1000):
    ans += cur + 1
    cur += 1
    cur %= 7
print(ans)