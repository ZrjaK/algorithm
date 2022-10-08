# 题目：1631.最小体力消耗路径
# 难度：MEDIUM
# 最后提交：2022-08-12 00:43:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dst = [[1e99] * n for _ in range(m)]
        dst[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            s, x, y = heappop(pq)
            for dx, dy in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0<=dx<m and 0<=dy<n:
                    t = max(s, abs(heights[x][y] - heights[dx][dy]))
                    if t < dst[dx][dy]:
                        dst[dx][dy] = t
                        heappush(pq, (t, dx, dy))
        return dst[-1][-1]
