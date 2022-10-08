# 题目：1465.切割后面积最大的蛋糕
# 难度：MEDIUM
# 最后提交：2022-08-30 20:40:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts += [0, h]
        horizontalCuts.sort()
        verticalCuts += [0, w]
        verticalCuts.sort()
        res = max(horizontalCuts[i]-horizontalCuts[i-1] for i in range(1, len(horizontalCuts))) * max(verticalCuts[i]-verticalCuts[i-1] for i in range(1, len(verticalCuts)))
        return res % (10**9+7)