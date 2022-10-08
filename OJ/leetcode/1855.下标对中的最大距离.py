# 题目：1855.下标对中的最大距离
# 难度：MEDIUM
# 最后提交：2022-05-16 12:48:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        ans = 0
        while i < len(nums1) and j < len(nums2):
            if j < i:
                j += 1
                continue
            if nums1[i] > nums2[j]:
                i += 1
                continue
            ans = max(ans, j-i)
            j += 1
        return ans