# 题目：2218.从栈中取出 K 个硬币的最大面值和
# 难度：HARD
# 最后提交：2022-03-27 17:16:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @functools.lru_cache(None)
        def process(curpos, k):
            if k == 0:
                return 0
            if dp[curpos][k]:
                return dp[curpos][k]
            if curpos == len(piles) - 1:
                if k > len(piles[-1]):
                    return -sys.maxsize
                dp[curpos][k] = sum(piles[-1][:k])
                return dp[curpos][k]
            base = 0
            res = process(curpos+1, k)
            for i in range(min(k, len(piles[curpos]))):
                base += piles[curpos][i]
                res = max(res, base+process(curpos+1, k-1-i))
            dp[curpos][k] = res
            return dp[curpos][k]


        dp = [[0] * (k+1) for _ in range(len(piles)+1)]
        return process(0, k)