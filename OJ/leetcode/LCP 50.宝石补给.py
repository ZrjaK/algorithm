# 题目：LCP 50.宝石补给
# 难度：EASY
# 最后提交：2022-04-16 15:03:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            t = gem[x] // 2
            gem[x] -= t
            gem[y] += t
        return max(gem)-min(gem)