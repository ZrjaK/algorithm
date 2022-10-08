# 题目：518.零钱兑换 II
# 难度：MEDIUM
# 最后提交：2022-04-14 04:58:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def p(index, rest):
            if rest == 0:
                return 1
            if index == len(coins):
                return 0
            res = 0
            for i in range(rest//coins[index]+1):
                res += p(index+1, rest-i*coins[index])
            return res
        return p(0, amount)