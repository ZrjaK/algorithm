# 题目：1814.统计一个数组中好对子的数目
# 难度：MEDIUM
# 最后提交：2023-01-18 00:20:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        for i in nums:
            t = i - int(str(i)[::-1])
            ans += d[t]
            d[t] += 1
        return ans % int(1e9+7)