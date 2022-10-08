# 题目：1608.特殊数组的特征值
# 难度：EASY
# 最后提交：2022-09-12 00:03:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for ans in range(1001):
            if len([i for i in nums if i >= ans]) == ans:
                return ans
        return -1