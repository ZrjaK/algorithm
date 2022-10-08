# 题目：1476.子矩形查询
# 难度：MEDIUM
# 最后提交：2022-09-12 20:43:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.m = rectangle
        self.u = []


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.u.append((row1, col1, row2, col2, newValue))


    def getValue(self, row: int, col: int) -> int:
        for i in range(len(self.u)-1, -1, -1):
            row1, col1, row2, col2, v = self.u[i]
            if row1 <= row <= row2 and col1 <= col <= col2:
                return v
        return self.m[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)