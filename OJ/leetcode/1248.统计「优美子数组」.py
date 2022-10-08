# 题目：1248.统计「优美子数组」
# 难度：MEDIUM
# 最后提交：2022-05-23 10:39:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = [0] * (len(nums)+1)
        d[0] = 1
        ans = 0
        pre = 0
        for i in nums:
            pre += i % 2
            d[pre] += 1
            if pre >= k:
                ans += d[pre-k]
        return ans