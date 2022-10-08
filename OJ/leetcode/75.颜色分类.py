# 题目：75.颜色分类
# 难度：MEDIUM
# 最后提交：2022-05-26 11:05:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n0 = n1 = n2 = 0
        for i in nums:
            if i == 0:
                n0 += 1
            elif i == 1:
                n1 += 1
            else:
                n2 += 1
        for i in range(len(nums)):
            if n0:
                nums[i] = 0
                n0 -= 1
            elif n1:
                nums[i] = 1
                n1 -= 1
            else:
                nums[i] = 2
                