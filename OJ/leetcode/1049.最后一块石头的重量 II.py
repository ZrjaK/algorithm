# 题目：1049.最后一块石头的重量 II
# 难度：MEDIUM
# 最后提交：2022-07-13 02:42:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        @cache
        def p(i, rest):
            if rest < 0:
                return -1e99
            if i == len(stones):
                return 0
            return max(p(i+1, rest), p(i+1, rest-stones[i])+stones[i])
        return s-p(0, s//2)*2