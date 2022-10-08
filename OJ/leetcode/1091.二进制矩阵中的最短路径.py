# 题目：1091.二进制矩阵中的最短路径
# 难度：MEDIUM
# 最后提交：2022-08-05 03:37:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = []
        if not grid[0][0]:
            pq.append((1, 0, 0))
        v = set()
        while pq:
            t, x, y = heappop(pq)
            if x == n-1 and y == n-1:
                return t
            if (x, y) in v:
                continue
            v.add((x, y))
            for dx in [x-1, x, x+1]:
                for dy in [y-1, y, y+1]:
                    if 0<=dx<n and 0<=dy<n and not grid[dx][dy]:
                        heappush(pq, (t+1, dx, dy))
        return -1