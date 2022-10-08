# 题目：1637.两点之间不包含任何点的最宽垂直面积
# 难度：MEDIUM
# 最后提交：2022-08-31 16:43:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        return max([points[i][0]-points[i-1][0] for i in range(1, len(points))])