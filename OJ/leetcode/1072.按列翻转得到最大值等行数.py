# 题目：1072.按列翻转得到最大值等行数
# 难度：MEDIUM
# 最后提交：2022-09-12 14:22:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = defaultdict(int)
        for i in matrix:
            d[tuple(i)] += 1
            d[tuple(j^1 for j in i)] += 1
        return max(d.values())