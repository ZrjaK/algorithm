a, n = input().split()
n = int(n)
b = [list(input()) for _ in range(n)]
arr = [i[::-1] for i in b][::-1]
if b == arr:
    print("bu yong dao le")

for i in range(n):
    for j in range(n):
        if arr[i][j] != " ":
            arr[i][j] = a
for i in arr:
    print("".join(i))