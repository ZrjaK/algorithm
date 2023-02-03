n, m = map(int, input().split())
for _ in range(n):
    s = input()
    if "qiandao" in s or "easy" in s:
        continue
    if not m:
        exit(print(s))
    m -= 1
print("Wo AK le")