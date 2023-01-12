# 题目：2492.两个城市间路径的最小分数
# 难度：MEDIUM
# 最后提交：2022-12-04 19:13:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        for a, b, c in roads:
            d[a].append((b, c))
            d[b].append((a, c))
        ans = inf
        vis = [False] * (n+1)
        def dfs(u) -> None:
            nonlocal ans
            vis[u] = True
            for v, w in d[u]:
                ans = min(ans, w)
                if not vis[v]:
                    dfs(v)
        dfs(1)
        return ans