def fib(n):
    if n <= 1:
        return n
    m = [[1, 1], [1, 0]]
    res = powMatrix(m, n-2)
    return res[0][0] + res[1][0]

def powMatrix(m, p):
    res = [[0] * len(m[0]) for _ in range(len(m))]
    for i in range(len(m)):
        res[i][i] = 1
    t = m
    while p:
        if p & 1:
            res = mulMatrix(res, t)
        t = mulMatrix(t, t)
        p >>= 1
    return res

def mulMatrix(m1, m2):
    res = [[0] * len(m2[0]) for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2)):
            for k in range(len(m2[0])):
                res[i][k] += m1[i][j] * m2[j][k]
    return res