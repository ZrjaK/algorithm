# 题目：1905.统计子岛屿
# 难度：MEDIUM
# 最后提交：2022-08-12 00:57:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    flag = 1
                    q = deque([[i, j]])
                    grid2[i][j] = 0
                    while q:
                        x, y = q.popleft()
                        if not grid1[x][y]:
                            flag = 0
                        for dx, dy in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                            if 0<=dx<m and 0<=dy<n and grid2[dx][dy]:
                                grid2[dx][dy] = 0
                                q.append((dx, dy))
                    ans += flag
        return ans