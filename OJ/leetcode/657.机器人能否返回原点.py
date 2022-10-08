# 题目：657.机器人能否返回原点
# 难度：EASY
# 最后提交：2021-10-23 12:32:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')