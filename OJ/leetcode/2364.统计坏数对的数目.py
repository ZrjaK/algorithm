# 题目：2364.统计坏数对的数目
# 难度：MEDIUM
# 最后提交：2022-08-06 23:12:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        ans = 0
        for i in range(n):
            ans += d[nums[i]-i]
            d[nums[i]-i] += 1
        return n*(n-1)//2 - ans
            