# 题目：2543.判断一个点是否可以到达
# 难度：HARD
# 最后提交：2023-01-22 00:50:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        return gcd(targetX, targetY).bit_count() == 1