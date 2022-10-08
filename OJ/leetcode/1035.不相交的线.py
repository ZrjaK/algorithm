# 题目：1035.不相交的线
# 难度：MEDIUM
# 最后提交：2022-09-05 15:58:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        @cache
        def p(x, y):
            res = 0
            for i in range(x, m):
                for j in range(y, n):
                    if nums1[i] == nums2[j]:
                        res = max(res, 1 + p(i+1, j+1))
            return res
        return p(0, 0)