# 题目：2202.K 次操作后最大化顶端元素
# 难度：MEDIUM
# 最后提交：2022-09-09 18:31:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = -1
        if n == 1:
            if k % 2:
                return -1
            else:
                return nums[0]
        for i in range(min(n, k + 1)):
            if i != k - 1:
                res = max(res, nums[i])
        return res