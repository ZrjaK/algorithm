# 题目：剑指 Offer II 010.和为 k 的子数组
# 难度：MEDIUM
# 最后提交：2022-10-04 16:20:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = list(accumulate(nums))
        ans = 0
        d = defaultdict(int)
        d[0] += 1
        for i in h:
            ans += d[i-k]
            d[i] += 1
        return ans