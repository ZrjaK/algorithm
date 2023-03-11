# 题目：2363.合并相似的物品
# 难度：EASY
# 最后提交：2023-02-28 09:54:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for i, j in items1:
            d[i] += j
        for i, j in items2:
            d[i] += j
        res = []
        for i in d.keys():
            res.append([i, d[i]])
        res.sort()
        return res