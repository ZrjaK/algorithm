# 题目：836.矩形重叠
# 难度：EASY
# 最后提交：2021-10-25 15:06:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2=rec1
        x3,y3,x4,y4=rec2
        return (x3-x2)*(x4-x1)<0 and (y3-y2)*(y4-y1)<0
        