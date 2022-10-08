# 题目：2226.每个小孩最多能分到多少糖果
# 难度：MEDIUM
# 最后提交：2022-04-03 13:43:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, int(1e8)
        while l < r:
            m = l + r >> 1
            if sum(i//m for i in candies) >= k:
                l = m+1
            else:
                r = m
        return l-1