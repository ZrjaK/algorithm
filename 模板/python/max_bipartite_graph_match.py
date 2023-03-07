def max_bipartite_graph_match(n, m, E):
    match = [-1] * (n + m)
    vis = [0] * (n + m)
    def dfs(i):
        for j in E[i]:
            if not vis[j]:
                vis[j] = 1
                if match[j] == -1 or dfs(match[j]):
                    match[j] = i
                    return 1
        return 0
    ans = 0
    for i in range(n):
        vis = [0] * (n + m)
        ans += dfs(i)
    return ans