# 题目：1523.在区间范围内统计奇数数目
# 难度：EASY
# 最后提交：2021-10-19 23:54:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 1 or low % 2 == 1:
            return (high - low) // 2 + 1
        else :
            return (high - low) // 2