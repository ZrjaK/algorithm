# 题目：1887.使数组元素相等的减少操作次数
# 难度：MEDIUM
# 最后提交：2022-09-01 03:54:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0   # 总操作次数
        cnt = 0   # 每个元素操作次数
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                cnt += 1
            res += cnt
        return res