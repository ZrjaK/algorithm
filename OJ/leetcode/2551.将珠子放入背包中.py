# 题目：2551.将珠子放入背包中
# 难度：HARD
# 最后提交：2023-01-29 17:06:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        l = sorted(a + b for a, b in pairwise(weights))
        return sum(l[-(k-1):]) - sum(l[:(k-1)])