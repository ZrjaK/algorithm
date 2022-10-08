# 题目：88.合并两个有序数组
# 难度：EASY
# 最后提交：2021-10-20 22:03:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()