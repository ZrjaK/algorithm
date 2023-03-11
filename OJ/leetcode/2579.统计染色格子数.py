# 题目：2579.统计染色格子数
# 难度：MEDIUM
# 最后提交：2023-03-04 22:35:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        for i in range(2, n+1):
            ans += (i-1) * 4
        return ans