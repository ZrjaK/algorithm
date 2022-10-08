# 题目：1401.圆和矩形是否有重叠
# 难度：MEDIUM
# 最后提交：2022-03-25 20:08:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        a = max(0, x1 - x_center, x_center - x2) ** 2 
        b = max(0, y1 - y_center, y_center - y2) ** 2
        c = radius ** 2
        return a + b <= c