# 题目：1140.石子游戏 II
# 难度：MEDIUM
# 最后提交：2022-07-13 14:10:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @cache
        def p(i, m): # i及其往后的石子中，取[1,2m]个，最多比另一个人多拿多少石子
            if n-i <= 2*m:
                return sum(piles[i:])
            res = -1e99
            for j in range(1, 2*m+1):
                res = max(res, -p(i+j, max(m, j)) + sum(piles[i:i+j]))
            return res
        return (sum(piles)+p(0, 1)) // 2