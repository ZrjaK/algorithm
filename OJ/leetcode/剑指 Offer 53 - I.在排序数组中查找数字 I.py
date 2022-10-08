# 题目：剑指 Offer 53 - I.在排序数组中查找数字 I
# 难度：EASY
# 最后提交：2022-10-03 18:59:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect_right(nums, target) - bisect_left(nums, target)