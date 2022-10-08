# 题目：496.下一个更大元素 I
# 难度：EASY
# 最后提交：2021-10-22 13:49:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]), len(nums2)):
                if nums1[i] < nums2[j]:
                    l.append(nums2[j])
                    break         
            else:
                l.append(-1)
        return l