n = int(input())
h = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        h.append(i)
        h.append(n//i)
h.sort()
h = h[1:]
ans = []
for i in range(len(h)):
    tmp = [h[i]]
    t = n // h[i]
    for j in range(i+1, len(h)):
        if t % h[j] != 0 or h[j] != tmp[-1] + 1:
            break
        tmp.append(h[j])
        t //= h[j]
    if len(tmp) > len(ans):
        ans = tmp[:]
if not ans:
    ans = [n]
print(len(ans))
print("*".join(map(str, ans)))