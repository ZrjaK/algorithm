# 题目：2541.使数组中所有元素相等的最小操作数 II
# 难度：MEDIUM
# 最后提交：2023-01-22 00:27:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        ans = 0
        c = 0
        for i, j in zip(nums1, nums2):
            if (i - j) % k != 0:
                return -1
            if i > j:
                ans += (i - j) // k
            c += (i - j) // k
        if c != 0:
            return -1
        return ans