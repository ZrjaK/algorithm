# 题目：2171.拿出最少数目的魔法豆
# 难度：MEDIUM
# 最后提交：2022-09-01 16:34:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        h = list(accumulate(beans)) + [0]
        ans = 1e99
        n = len(beans)
        for i in range(n):
            ans = min(ans ,h[i-1] + h[n-1] - h[i] - beans[i] * (n-i-1))
        return ans