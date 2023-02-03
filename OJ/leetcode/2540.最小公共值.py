# 题目：2540.最小公共值
# 难度：EASY
# 最后提交：2023-01-22 00:24:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort(reverse=1)
        nums2.sort(reverse=1)
        while nums1 and nums2:
            if nums1[-1] == nums2[-1]:
                return nums1.pop()
            elif nums1[-1] < nums2[-1]:
                nums1.pop()
            else:
                nums2.pop()
        return -1
        