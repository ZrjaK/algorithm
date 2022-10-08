# 题目：2419.按位与最大的最长子数组
# 难度：MEDIUM
# 最后提交：2022-09-25 11:20:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        n = len(nums)
        ans = 1
        h = []
        for i in nums:
            if h and i & h[-1] == target:
                h.append(target)
                ans = max(ans, len(h))
            else:
                h = [i]
        h = []
        for i in nums[::-1]:
            if h and i & h[-1] == target:
                h.append(target)
                ans = max(ans, len(h))
            else:
                h = [i]
        
        return ans