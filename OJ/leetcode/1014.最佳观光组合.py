# 题目：1014.最佳观光组合
# 难度：MEDIUM
# 最后提交：2022-03-25 04:53:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left = values[0] - 0
        res = 0
        for i in range(1, len(values)):
            res = max(res, left + values[i] - i)
            left = max(left, values[i] + i)
        return res