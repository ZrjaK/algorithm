# 题目：974.和可被 K 整除的子数组
# 难度：MEDIUM
# 最后提交：2023-01-03 22:31:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s = 0
        d = defaultdict(int)
        d[0] += 1
        ans = 0
        for i in nums:
            s += i
            ans += d[s % k]
            d[s % k] += 1
        return ans