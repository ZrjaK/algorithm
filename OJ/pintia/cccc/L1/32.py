n, a = input().split()
n = int(n)
s = input()
ans = s[-n:]
ans = a * (n - len(ans)) + ans
print(ans)