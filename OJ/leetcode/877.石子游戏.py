# 题目：877.石子游戏
# 难度：MEDIUM
# 最后提交：2022-07-08 15:22:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def p(i, j):
            if i == j:
                return piles[i]
            return max(piles[i] - p(i+1, j), piles[j] - p(i, j-1))
        return p(0, len(piles)-1) > 0