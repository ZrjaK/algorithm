n = int(input())
arr = [float(i) for i in input().split()]
ans = []
for i in range(1, n):
    x = (arr[i] - arr[i - 1]) / arr[i - 1]
    ans.append("%.15f" % x)
print(*ans, end="")
    