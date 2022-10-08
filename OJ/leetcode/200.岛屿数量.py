# 题目：200.岛屿数量
# 难度：MEDIUM
# 最后提交：2022-07-27 01:10:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                visited = set()
                q = deque([[i, j]])
                while q:
                    x, y = q.popleft()
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    grid[x][y] = "0"
                    if 0<=x-1<m and grid[x-1][y] == "1":
                        q.append([x-1,y])
                    if 0<=x+1<m and grid[x+1][y] == "1":
                        q.append([x+1,y])
                    if 0<=y-1<n and grid[x][y-1] == "1":
                        q.append([x,y-1])
                    if 0<=y+1<n and grid[x][y+1] == "1":
                        q.append([x,y+1])
                ans += 1
        return ans