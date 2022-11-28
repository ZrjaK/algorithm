from copy import deepcopy

# m 为 n行 n + 1列的增广矩阵
# a[i][n] for i in range(n)即为各个未知数的解
def gauss(m):
    a = deepcopy(m)
    n = len(a)
    for r in range(n):
        c = r
        t = r
        for i in range(r+1, n):
            if abs(a[i][c]) > abs(a[t][c]):
                t = i
        for i in range(c, n+1):
            a[r][i], a[t][i] = a[t][i], a[r][i]
        for i in range(n, c-1, -1):
            a[r][i] /= a[r][c]
        for i in range(r+1, n):
            for j in range(n, c-1, -1):
                a[i][j] -= a[r][j] * a[i][c]
    for i in range(n-1, 0, -1):
        for j in range(i-1, -1, -1):
            a[j][n] -= a[i][n] * a[j][i]
            a[j][i] = 0
    return a