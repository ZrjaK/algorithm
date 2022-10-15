# 题目：956.最高的广告牌
# 难度：HARD
# 最后提交：2022-10-13 16:20:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        @cache
        def p(i, s):
            if i == n:
                return 0 if s == 0 else -1e99
            return max(p(i+1, s), rods[i] + p(i+1, s+rods[i]), p(i+1, s-rods[i]))
        return p(0, 0)