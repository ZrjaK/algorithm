# 题目：2017.网格游戏
# 难度：MEDIUM
# 最后提交：2022-09-13 09:14:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = 1e99
        a = sum(grid[0])
        b = -grid[1][-1]
        for i in range(n):
            a -= grid[0][i]
            b += grid[1][i-1]
            ans = min(ans, max(a, b))
        return ans