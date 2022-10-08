# 题目：1232.缀点成线
# 难度：EASY
# 最后提交：2021-11-13 22:21:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for x, y in coordinates[2:]:
            if (y0 - y1) * (x1 - x) != (x0 - x1) * (y1 - y):
                return False
        return True