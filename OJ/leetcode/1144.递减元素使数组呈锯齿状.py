# 题目：1144.递减元素使数组呈锯齿状
# 难度：MEDIUM
# 最后提交：2023-02-27 00:00:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n, t = len(nums), [0, 0]
        for k in [0, 1]:
            for i in range(k, n, 2):
                d = 0
                if i > 0:
                    d = max(d, nums[i] - nums[i - 1] + 1)
                if i + 1 < n:
                    d = max(d, nums[i] - nums[i + 1] + 1)
                t[k] += d
        return min(t)