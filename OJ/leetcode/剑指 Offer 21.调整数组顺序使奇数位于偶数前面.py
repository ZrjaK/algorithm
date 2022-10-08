# 题目：剑指 Offer 21.调整数组顺序使奇数位于偶数前面
# 难度：EASY
# 最后提交：2022-10-01 16:44:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        return [i for i in nums if i % 2] + [i for i in nums if i % 2 == 0]