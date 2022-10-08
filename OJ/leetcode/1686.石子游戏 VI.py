# 题目：1686.石子游戏 VI
# 难度：MEDIUM
# 最后提交：2022-09-14 14:49:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        h = [(a+b) for a,b in zip(aliceValues, bobValues)]
        h.sort(reverse=True)
        ans = sum(h[::2]) - sum(bobValues)
        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        return 0
