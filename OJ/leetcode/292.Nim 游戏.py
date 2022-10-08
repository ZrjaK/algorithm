# 题目：292.Nim 游戏
# 难度：EASY
# 最后提交：2021-10-21 17:46:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canWinNim(self, n: int) -> bool:
        return bool(n % 4)