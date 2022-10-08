# 题目：剑指 Offer 60.n个骰子的点数
# 难度：MEDIUM
# 最后提交：2022-10-03 20:55:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        @cache
        def p(rest, c):
            if rest == 0:
                return int(c == 0)
            return sum(p(rest-1, c-j) for j in range(1, 7))
        ans = [0] * (6*n+1-n)
        for i in range(n, 6*n+1):
            ans[i-n] = p(n, i) / 6**n
        return ans