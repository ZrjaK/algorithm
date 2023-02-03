from collections import Counter


s = input().upper()
c = Counter(s)
d = "GPLT"
f = 0
ans = []
while c["G"] or c["P"] or c["T"] or c["L"]:
    if c[d[f]]:
        ans += d[f]
        c[d[f]] -= 1
    f = (f + 1) % 4
print("".join(ans))