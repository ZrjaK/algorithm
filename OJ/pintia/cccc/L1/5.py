n = int(input())
d = {}
for _ in range(n):
    s = input().split()
    d[int(s[1])] = s[0] + " " + s[2]
input()
arr = list(map(int, input().split()))
for i in arr:
    print(d[i])