n = 10**5

parent = list(range(n))
cnt = [1] * n

def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    x, y = find(i), find(j)
    if x != y:
        cnt[y] += cnt[x]
        parent[x] = parent[y]