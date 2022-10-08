a, b, k = [int(i) for i in input().split()]
ans = 0
while a < b:
    a *= k
    ans += 1
print(ans)