# 题目：2290.到达角落需要移除障碍物的最小数目
# 难度：HARD
# 最后提交：2022-09-21 10:29:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[1e99] * n for _ in range(m)]
        dist[-1][-1] = 0
        pq = [[0, m-1, n-1]]
        v = set()
        while pq:
            d, x, y = heappop(pq)
            if dist[x][y] < d:
                continue
            for nx, ny in [[x-1, y], [x+1, y], [x, y+1], [x, y-1]]:
                if 0<=nx<m and 0<=ny<n and dist[x][y] + grid[nx][ny] < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + grid[nx][ny]
                    heappush(pq, [dist[nx][ny], nx, ny])
        return dist[0][0]