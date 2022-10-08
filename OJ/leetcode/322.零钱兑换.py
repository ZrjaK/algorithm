# 题目：322.零钱兑换
# 难度：MEDIUM
# 最后提交：2022-06-28 21:38:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort(reverse=True)
        @cache
        def p(rest):
            if rest < 0:
                return 1e99
            if rest == 0:
                return 0
            res = 1e99
            for i in coins:
                res = min(res, p(rest-i)+1)
            return res
        res = p(amount)
        return res if res < 1e90 else -1