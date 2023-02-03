# 题目：2303.计算应缴税款总额
# 难度：EASY
# 最后提交：2023-01-23 01:25:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        prei, prej = 0, 0
        for i, j in brackets:
            ans += (min(i, income)-prei) * j / 100
            prei = i
            if income < i:
                break
        return ans