# 题目：1254.统计封闭岛屿的数目
# 难度：MEDIUM
# 最后提交：2022-08-06 16:59:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        v = set()
        q = deque()
        for i in [0, m-1]:
            for j in range(n):
                if not grid[i][j]:
                    grid[i][j] = 1
                    q.append([i, j])
        for i in range(m):
            for j in [0, n-1]:
                if not grid[i][j]:
                    grid[i][j] = 1
                    q.append([i, j])
        while q:
            x, y = q.popleft()
            for dx, dy in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                if 0<=dx<m and 0<=dy<n and not grid[dx][dy]:
                    grid[dx][dy] = 1
                    q.append([dx, dy])
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    grid[i][j] = 1 
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        for dx, dy in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                            if 0<=dx<m and 0<=dy<n and not grid[dx][dy]:
                                grid[dx][dy] = 1
                                q.append([dx, dy])
                    ans += 1
        return ans