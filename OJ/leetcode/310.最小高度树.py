# 题目：310.最小高度树
# 难度：MEDIUM
# 最后提交：2022-07-27 16:48:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        d = defaultdict(list)
        degree = [0] * n
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
            degree[i] += 1
            degree[j] += 1

        q = [i for i, d in enumerate(degree) if d == 1]
        remainNodes = n
        while remainNodes > 2:
            remainNodes -= len(q)
            tmp = q
            q = []
            for x in tmp:
                for y in d[x]:
                    degree[y] -= 1
                    if degree[y] == 1:
                        q.append(y)
        return q