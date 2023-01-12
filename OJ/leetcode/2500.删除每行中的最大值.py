# 题目：2500.删除每行中的最大值
# 难度：EASY
# 最后提交：2022-12-11 13:42:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        for _ in range(m):
            ans += max(max(i) for i in grid)
            for i in range(n):
                grid[i].pop(grid[i].index(max(grid[i])))
        return ans