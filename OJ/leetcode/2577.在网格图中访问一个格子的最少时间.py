# 题目：2577.在网格图中访问一个格子的最少时间
# 难度：HARD
# 最后提交：2023-02-26 10:59:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dist = [[1e99] * m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            s, x, y = heappop(pq)
            if s != dist[x][y]:
                continue
            if x == n-1 and y == m-1:
                return s
            f = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0<=nx<n and 0<=ny<m and s + 1 >= grid[nx][ny]:
                    f = 1
            if f:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0<=nx<n and 0<=ny<m:
                        if s + 1 < grid[nx][ny]:
                            if s % 2 == grid[nx][ny] % 2:
                                ns = grid[nx][ny] + 1
                            else:
                                ns = grid[nx][ny]
                            if dist[nx][ny] > ns:
                                dist[nx][ny] = ns
                                heappush(pq, (ns, nx, ny))
                        else:
                            if dist[nx][ny] > s + 1:
                                dist[nx][ny] = s + 1
                                heappush(pq, (s + 1, nx, ny))
        return -1