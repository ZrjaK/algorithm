ans = 0
s = 1
for i in range(1, int(input())+1):
    s *= i
    ans += s
print(ans)