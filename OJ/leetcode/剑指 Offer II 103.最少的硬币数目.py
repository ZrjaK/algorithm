# 题目：剑指 Offer II 103.最少的硬币数目
# 难度：MEDIUM
# 最后提交：2022-10-10 10:29:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def p(i, rest):
            if rest == 0:
                return 0
            if i == n or rest < 0:
                return 1e99
            return min(1 + p(i, rest-coins[i]), p(i+1, rest))
        res = p(0, amount)
        return res if res != 1e99 else -1