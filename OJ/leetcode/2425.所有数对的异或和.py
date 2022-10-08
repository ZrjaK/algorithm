# 题目：2425.所有数对的异或和
# 难度：MEDIUM
# 最后提交：2022-10-01 22:51:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1) % 2, len(nums2) % 2
        if not n and not m:
            return 0
        ans = 0
        if n == 1:
            for i in nums2:
                ans ^= i
        if m == 1:
            for i in nums1:
                ans ^= i
        return ans
        