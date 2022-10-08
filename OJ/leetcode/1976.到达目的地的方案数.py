# 题目：1976.到达目的地的方案数
# 难度：MEDIUM
# 最后提交：2022-07-22 03:09:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        d = [[1e99] * n for _ in range(n)]
        for i, j, w in roads:
            d[i][j] = w
            d[j][i] = w
            d[i][i] = d[j][j] = 0
        mindst = [1e99] * n
        mindst[0] = 0
        minHeap = [(0, 0)]
        while minHeap:
            distance, node = heapq.heappop(minHeap)
            for i in range(n):
                if d[node][i] == 1e99:
                    continue
                if mindst[node] + d[node][i] < mindst[i]:
                    mindst[i] = mindst[node] + d[node][i]
                    heapq.heappush(minHeap, (d[i][node] + d[node][n-1], i))

        g = defaultdict(list)
        for x, y, z in roads:
            if mindst[y] - mindst[x] == z:
                g[x].append(y)
            elif mindst[x] - mindst[y] == z:
                g[y].append(x)

        @cache
        def dfs(u: int) -> int:
            if u == n - 1:
                return 1

            ret = 0
            for v in g[u]:
                ret += dfs(v)
            return ret
        
        ans = dfs(0)
        dfs.cache_clear()
        return ans % int(1e9+7)