# 题目：2449.使数组相似的最少操作次数
# 难度：HARD
# 最后提交：2022-10-23 12:00:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums_odd = sorted([x for x in nums if x % 2])
        nums_even = sorted([x for x in nums if x % 2 == 0])
        target_odd = sorted([x for x in target if x % 2])
        target_even = sorted([x for x in target if x % 2 == 0])
        ans = 0
        ans += sum(abs(x-y) // 2 for x, y in zip(nums_odd, target_odd))
        ans += sum(abs(x-y) // 2 for x, y in zip(nums_even, target_even))
        return ans // 2