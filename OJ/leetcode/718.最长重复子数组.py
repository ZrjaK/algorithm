# 题目：718.最长重复子数组
# 难度：MEDIUM
# 最后提交：2022-05-01 22:02:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return max(max(i) for i in dp)