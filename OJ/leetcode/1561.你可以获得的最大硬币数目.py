# 题目：1561.你可以获得的最大硬币数目
# 难度：MEDIUM
# 最后提交：2022-05-07 23:59:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        t = piles[len(piles)//3:]
        return sum(t[::2])