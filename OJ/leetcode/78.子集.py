# 题目：78.子集
# 难度：MEDIUM
# 最后提交：2022-08-24 16:44:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(1<<n):
            t = []
            for j in range(n):
                if 1<<j & i:
                    t.append(nums[j])
            res.append(t)
        return res