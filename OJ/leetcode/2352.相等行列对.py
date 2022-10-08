# 题目：2352.相等行列对
# 难度：MEDIUM
# 最后提交：2022-07-24 10:36:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = defaultdict(int)
        for i in grid:
            d[tuple(i)] += 1
        ans = 0
        for j in range(n):
            t = [grid[i][j] for i in range(n)]
            if tuple(t) in d:
                ans += d[tuple(t)]
        return ans