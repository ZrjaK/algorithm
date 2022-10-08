# 题目：365.水壶问题
# 难度：MEDIUM
# 最后提交：2022-07-28 17:05:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if x+y < z:
            return False
        if x>y:
            x,y=y,x
        if x == 0:
            return y==z
        while y%x != 0:
            y,x = x,y%x
        return z%x==0