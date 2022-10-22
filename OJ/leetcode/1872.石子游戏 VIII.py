# 题目：1872.石子游戏 VIII
# 难度：HARD
# 最后提交：2022-10-17 16:39:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        h = list(accumulate(stones))
        n = len(stones)
        @cache
        def p(i):
            if i == n-1:
                return h[n-1]
            return max(p(i+1), h[i]-p(i+1))
        return p(1)