# 题目：2215.找出两数组的不同
# 难度：EASY
# 最后提交：2022-03-27 10:34:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        com = set()
        for i in nums1:
            if i in nums2:
                com.add(i)
        for i in com:
            if i in nums1:
                s1.remove(i)
            if i in nums2:
                s2.remove(i)
        return [list(s1),list(s2)]