# 题目：674.最长连续递增序列
# 难度：EASY
# 最后提交：2021-10-23 12:45:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        begin = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                res = max(res, i - begin + 1)
                begin = i + 1
                continue
            res = max(res, i - begin + 2)
        return res