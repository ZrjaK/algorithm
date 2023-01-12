# 题目：1812.判断国际象棋棋盘中一个格子的颜色
# 难度：EASY
# 最后提交：2022-12-08 11:07:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return int(ord(coordinates[0]) ^ (int(coordinates[1]) % 2 & 1) ) % 2 == 1