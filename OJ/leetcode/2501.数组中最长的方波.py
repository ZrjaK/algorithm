# 题目：2501.数组中最长的方波
# 难度：MEDIUM
# 最后提交：2022-12-11 13:44:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        d = defaultdict(int)
        for i in nums:
            d[i] = d[i**0.5] + 1
        res = max(d.values())
        return res if res > 1 else -1