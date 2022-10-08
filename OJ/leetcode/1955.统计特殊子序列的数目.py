# 题目：1955.统计特殊子序列的数目
# 难度：HARD
# 最后提交：2022-09-20 08:59:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        f0 = f01 = f012 = 0
        for i in nums:
            if i == 0:
                f0 += f0 + 1
            elif i == 1:
                f01 += f01 + f0
            else:
                f012 += f012 + f01
        return f012 % int(1e9+7)