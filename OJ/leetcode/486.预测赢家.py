# 题目：486.预测赢家
# 难度：MEDIUM
# 最后提交：2022-07-05 18:29:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def p(i, j):
            if i == j:
                return nums[i]
            return max(nums[i] - p(i+1, j), nums[j] - p(i, j-1))
        return p(0, len(nums)-1) >= 0