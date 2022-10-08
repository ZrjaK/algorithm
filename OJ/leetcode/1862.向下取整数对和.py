# 题目：1862.向下取整数对和
# 难度：HARD
# 最后提交：2022-09-21 16:59:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        ma = max(nums)
        cnt = [0] * (ma+1)
        for i in nums:
            cnt[i] += 1
        h = [0] * (ma+1)
        for i in range(ma+1):
            h[i] = h[i-1] + cnt[i]
        ans = 0
        for i in list(set(nums)):
            d = 1
            while d * i <= ma:
                ans += cnt[i] * d * (h[min(ma, (d+1)*i-1)] - h[d*i-1])
                d += 1
        return ans % int(1e9+7)