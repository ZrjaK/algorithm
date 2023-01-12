# 题目：2025.分割数组的最多方案数
# 难度：HARD
# 最后提交：2023-01-09 03:36:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = list(accumulate(nums))
        cl = defaultdict(int)
        cr = defaultdict(int)
        for i in range(n-1):
            cr[h[i]] += 1
        ans = 0
        if h[-1] % 2 == 0:
            ans = cr[h[-1]>>1]
        for i in range(n):
            d = k - nums[i]
            if (h[-1] + d) % 2 == 0:
                ans = max(ans, cl[h[-1]+d>>1]+cr[h[-1]-d>>1])
            cl[h[i]] += 1
            cr[h[i]] -= 1
        return ans