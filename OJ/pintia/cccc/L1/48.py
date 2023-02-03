ra, ca = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(ra)]

rb, cb = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(rb)]

if ca != rb:
    exit(print(f"Error: {ca} != {rb}"))

def mulMatrix(m1, m2):
    res = [[0] * len(m2[0]) for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2)):
            for k in range(len(m2[0])):
                res[i][k] += m1[i][j] * m2[j][k]
    return res
ans = mulMatrix(a, b)
print(ra, cb)
for i in ans:
    print(*i)