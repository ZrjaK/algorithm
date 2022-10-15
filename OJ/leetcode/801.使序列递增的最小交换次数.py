# 题目：801.使序列递增的最小交换次数
# 难度：HARD
# 最后提交：2022-10-10 00:29:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1 += [-1]
        nums2 += [-1]
        @cache
        def p(i, preswap):
            if i == n:
                return 0
            res = 1e99
            a, b = nums1[i-1], nums2[i-1]
            if preswap:
                a, b = b, a
            if nums1[i] > a and nums2[i] > b:
                res = min(res, p(i+1, False))
            if nums1[i] > b and nums2[i] > a:
                res = min(res, 1+p(i+1, True))
            return res
        return p(0, False)