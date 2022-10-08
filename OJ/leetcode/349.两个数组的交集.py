# 题目：349.两个数组的交集
# 难度：EASY
# 最后提交：2021-10-21 18:53:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))