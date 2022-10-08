# 题目：1368.使网格图至少有一条有效路径的最小代价
# 难度：HARD
# 最后提交：2022-09-17 11:15:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = {1: lambda x, y: [x, y+1],
            2: lambda x, y: [x, y-1],
            3: lambda x, y: [x+1, y],
            4: lambda x, y: [x-1, y]}
        pq = [(0, 0, 0)]
        v = set()
        while pq:
            s, x, y = heappop(pq)
            if x == m-1 and y == n-1:
                return s
            if (x, y) in v:
                continue
            else:
                v.add((x, y))
            for i in range(1, 5):
                nx, ny = d[i](x, y)
                if 0<=nx<m and 0<=ny<n:
                    heappush(pq, (s+(grid[x][y]!=i), nx, ny))
