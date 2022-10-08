# 题目：2256.最小平均差
# 难度：MEDIUM
# 最后提交：2022-04-30 22:43:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        h = [nums[0]]
        for i in nums[1:]:
            h.append(i+h[-1])
        res = []
        for i in range(n):
            if i == n-1:
                t = h[i]//(i+1)
            else:
                t = abs(h[i]//(i+1) - (h[-1]-h[i])//(n-i-1))
            res.append(t)
        return res.index(min(res))