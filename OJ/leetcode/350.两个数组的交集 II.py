# 题目：350.两个数组的交集 II
# 难度：EASY
# 最后提交：2021-10-21 18:54:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = set(nums1) & set(nums2)
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i), nums2.count(i))  
        return l