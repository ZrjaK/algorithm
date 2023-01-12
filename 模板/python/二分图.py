def bipartite(E):
    n = len(E)
    color = [0] * n
    for i in range(n):
        if not color[i]:
            q = deque([i])
            color[i] = 1
            while q:
                i = q.popleft()
                for j in E[i]:
                    if not color[j]:
                        color[j] = -color[i]
                        q.append(j)
                    elif color[j] == color[i]:
                        return []
    return color