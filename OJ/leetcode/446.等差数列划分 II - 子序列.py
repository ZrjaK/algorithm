# 题目：446.等差数列划分 II - 子序列
# 难度：HARD
# 最后提交：2022-12-11 21:44:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        ans = 0
        for i in range(n):
            for j in range(i):
                ans += d[j, nums[i]-nums[j]]
                d[i, nums[i]-nums[j]] += d[j, nums[i]-nums[j]] + 1
        return ans

