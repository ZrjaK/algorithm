# 题目：1391.检查网格中是否存在有效路径
# 难度：MEDIUM
# 最后提交：2022-08-09 02:30:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0)])
        v = set()
        while q:
            x, y = q.popleft()
            if (x, y) in v:
                continue
            v.add((x, y))
            if x == m-1 and y == n-1:
                return True
            if 0<=x-1<m and 0<=y<n and grid[x][y] in [2, 5, 6] and grid[x-1][y] in [2, 3, 4]:
                q.append((x-1, y))
            if 0<=x+1<m and 0<=y<n and grid[x][y] in [2, 3, 4] and grid[x+1][y] in [2, 5, 6]:
                q.append((x+1, y))
            if 0<=x<m and 0<=y+1<n and grid[x][y] in [1, 4, 6] and grid[x][y+1] in [1, 3, 5]:
                q.append((x, y+1))
            if 0<=x<m and 0<=y-1<n and grid[x][y] in [1, 3, 5] and grid[x][y-1] in [1, 4, 6]:
                q.append((x, y-1))
        return False