# 题目：2544.交替数字和
# 难度：EASY
# 最后提交：2023-01-22 14:07:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        f = 1
        for i in str(n):
            ans += f * int(i)
            f *= -1
        return ans