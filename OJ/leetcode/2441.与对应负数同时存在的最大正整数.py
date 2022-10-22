# 题目：2441.与对应负数同时存在的最大正整数
# 难度：EASY
# 最后提交：2022-10-16 10:30:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        v = set(nums)
        for i in nums[::-1]:
            if -i in v:
                return i
        return -1