n, op = input().split()
n = int(n)
h = []
cur = 1
while n >= (cur * 2 if cur != 1 else cur):
    h.append(cur)
    n -= (cur * 2 if cur != 1 else cur)
    cur += 2
t = h[-1]
ans = [" " * ((t-h[0])//2) + op * h[0]]
for i in h[1:]:
    ans.append(" " * ((t-i)//2) + op * i)
    ans.insert(0, " " * ((t-i)//2) + op * i)
print(*ans, sep='\n')
print(n)