# 题目：1539.第 k 个缺失的正整数
# 难度：EASY
# 最后提交：2021-10-20 00:29:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lostarr = []
        for i in range(1, 2001):
            if i not in arr:
                lostarr.append(i)
        return lostarr[k-1]