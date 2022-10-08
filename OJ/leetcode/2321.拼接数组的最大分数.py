# 题目：2321.拼接数组的最大分数
# 难度：HARD
# 最后提交：2022-06-26 12:22:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def p(a):
            res, dp = 0, 0
            for i in a:
                dp += i
                if dp < 0:
                    dp = 0
                res = max(res, dp)
            return res
        n = len(nums1)
        f = [0] * n

        s = 0
        for i in range(n):
            f[i] = nums2[i] - nums1[i]
            s += nums1[i]
        ans = s + p(f)

        s = 0
        for i in range(n):
            f[i] = nums1[i] - nums2[i]
            s += nums2[i]
        ans = max(ans, s + p(f))
        return ans
        