# 题目：1621.大小为 K 的不重叠线段的数目
# 难度：MEDIUM
# 最后提交：2022-07-19 00:23:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:    
    def numberOfSets(self, n: int, k: int) -> int:
        @cache
        def dp(n, k):
            if n < 2 or k > n-1:
                return 0
            if k == 1:
                return n * (n-1) // 2
            return 2*dp(n-1, k) + dp(n-1, k-1) - dp(n-2, k)

        return dp(n, k) % int(1e9+7)
