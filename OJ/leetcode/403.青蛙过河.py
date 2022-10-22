# 题目：403.青蛙过河
# 难度：HARD
# 最后提交：2022-10-20 15:01:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = set(stones)
        @cache
        def p(i, k):
            if k < 0 or i > stones[-1]:
                return False
            if i == stones[-1]:
                return True
            res = False
            if i+k-1 in d:
                res |= p(i+k-1, k-1)
            if k > 0 and i+k in d:
                res |= p(i+k, k)
            if i+k+1 in d:
                res |= p(i+k+1, k+1)
            return res
        return p(stones[0], 0)