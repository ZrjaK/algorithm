def topological_sort(E):
    n = len(E)
    ind = [0] * n
    for i in range(n):
        for j in E[i]:
            ind[j] += 1
    q = deque([i for i in range(n) if not ind[i]])
    g = []
    while q:
        i = q.popleft()
        g.append(i)
        for j in E[i]:
            ind[j] -= 1
            if not ind[j]:
                q.append(j)
    return g