# 题目：1051.高度检查器
# 难度：EASY
# 最后提交：2021-11-06 14:10:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([i != j for i, j in zip(heights, sorted(heights))])