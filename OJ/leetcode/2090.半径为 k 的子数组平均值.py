# 题目：2090.半径为 k 的子数组平均值
# 难度：MEDIUM
# 最后提交：2022-05-25 22:17:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        l = 0
        t = 2*k+1
        s = sum(nums[:t])
        if k < n-k:
            res[k] = s // t
        for r in range(2*k+1, n):
            s += nums[r]
            s -= nums[l]
            l += 1
            res[r-k] = s // t
        return res