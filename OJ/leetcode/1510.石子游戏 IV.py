# 题目：1510.石子游戏 IV
# 难度：HARD
# 最后提交：2022-12-15 18:53:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

@cache
def p(i):
    if i == 0:
        return False
    res = False
    for j in range(1, int(i**0.5)+1):
        res |= not p(i-j**2)
    return res
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return p(n)
