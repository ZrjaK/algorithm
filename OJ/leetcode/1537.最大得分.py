# 题目：1537.最大得分
# 难度：HARD
# 最后提交：2023-02-01 20:42:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp1, dp2 = [0] * (n+1), [0] * (m+1)
        i = j = 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                dp1[i+1] = max(dp1[i+1], dp1[i] + nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                dp2[j+1] = max(dp2[j+1], dp2[j] + nums2[j])
                j += 1
            else:
                t1, t2 = dp1[i], dp2[j]
                dp1[i+1] = max(dp1[i+1], max(dp1[i], dp2[j]) + nums1[i])
                dp2[j+1] = max(dp2[j+1], max(dp1[i], dp2[j]) + nums2[j])
                i += 1
                j += 1
        while i < n:
            dp1[i+1] = dp1[i] + nums1[i]
            i += 1
        while j < m:
            dp2[j+1] = dp2[j] + nums2[j]
            j += 1
        return max(dp1[n], dp2[m]) % int(1e9+7)


