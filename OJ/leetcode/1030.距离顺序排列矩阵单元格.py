# 题目：1030.距离顺序排列矩阵单元格
# 难度：EASY
# 最后提交：2021-11-05 21:54:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted(((i,j) for i in range(rows) for j in range(cols)), key=lambda p:abs(p[0]-rCenter)+abs(p[1]-cCenter))
