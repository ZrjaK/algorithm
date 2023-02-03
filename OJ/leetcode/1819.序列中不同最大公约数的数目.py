# 题目：1819.序列中不同最大公约数的数目
# 难度：HARD
# 最后提交：2023-01-14 03:26:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        ma = max(nums)
        v = set(nums)
        ans = 0
        for i in range(1, ma+1):
            h = [0]
            for j in range(i, ma+1, i):
                if j in v:
                    h.append(j)
            if reduce(gcd, h) == i:
                ans += 1
        return ans