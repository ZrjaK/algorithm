# 题目：2070.每一个查询的最大美丽值
# 难度：MEDIUM
# 最后提交：2022-05-18 22:57:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:x[1])
        items.sort(key=lambda x:x[0])
        # print(items)
        h1 = [i[0] for i in items]
        h2 = [items[0][1]]
        for i in range(1, len(items)):
            h2.append(max(h2[-1], items[i][1]))
        res = []
        for j in queries:
            t = bisect_right(h1, j)
            if t == 0:
                res.append(0)
                continue
            res.append(h2[t-1])
        return res