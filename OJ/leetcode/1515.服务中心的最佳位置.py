# 题目：1515.服务中心的最佳位置
# 难度：HARD
# 最后提交：2022-09-21 13:58:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

from scipy.optimize import minimize
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        return minimize(lambda t: sum([dist(p, t) for p in positions]), (0, 0))['fun']
