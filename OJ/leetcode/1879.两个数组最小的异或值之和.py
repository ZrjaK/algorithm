# 题目：1879.两个数组最小的异或值之和
# 难度：HARD
# 最后提交：2022-09-21 11:23:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        @cache
        def p(i, mask):
            if i == n:
                return 0
            res = 1e99
            for j in range(n):
                if not mask>>j & 1:
                    res = min(res, (nums1[i]^nums2[j])+p(i+1, mask|1<<j))
            return res
        return p(0, 0)