# 题目：剑指 Offer II 068.查找插入位置
# 难度：EASY
# 最后提交：2022-10-08 12:35:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)