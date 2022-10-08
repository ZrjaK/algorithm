# 题目：剑指 Offer 57.和为s的两个数字
# 难度：EASY
# 最后提交：2022-10-03 20:21:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v = set()
        for i in nums:
            if target - i in v:
                return [i, target-i]
            v.add(i)