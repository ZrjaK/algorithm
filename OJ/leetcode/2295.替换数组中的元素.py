# 题目：2295.替换数组中的元素
# 难度：MEDIUM
# 最后提交：2022-06-05 10:43:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {}
        n = len(nums)
        for i in range(n):
            d[nums[i]] = i
        for i, j in operations:
            nums[d[i]] = j
            d[j] = d[i]
        return nums
        