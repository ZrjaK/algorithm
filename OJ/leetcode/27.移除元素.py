# 题目：27.移除元素
# 难度：EASY
# 最后提交：2021-10-20 14:20:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)