# 题目：1090.受标签影响的最大值
# 难度：MEDIUM
# 最后提交：2022-08-30 03:38:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        d = defaultdict(list)
        for i, j in zip(values, labels):
            d[j].append(i)
        h = []
        for i in d:
            d[i].sort()
            h += d[i][-min(useLimit, len(d[i])):]
        return sum(sorted(h)[-numWanted:])