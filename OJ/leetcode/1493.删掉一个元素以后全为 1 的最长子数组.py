# 题目：1493.删掉一个元素以后全为 1 的最长子数组
# 难度：MEDIUM
# 最后提交：2022-05-24 13:31:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        c = 0
        ans = 0
        for r in range(len(nums)):
            if not nums[r]:
                c += 1
            while c > 1:
                if not nums[l]:
                    c -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans-1