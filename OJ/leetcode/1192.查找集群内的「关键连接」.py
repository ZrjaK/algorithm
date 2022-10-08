# 题目：1192.查找集群内的「关键连接」
# 难度：HARD
# 最后提交：2022-09-19 09:04:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        d = defaultdict(set)
        for i, j in connections:
            d[i].add(j)
            d[j].add(i)
        dfn = [0] * n
        low = [0] * n
        index = 0
        res = []
        v = set()
        def tarjan(i, father):
            nonlocal index
            index += 1
            dfn[i] = low[i] = index
            v.add(i)
            for j in d[i]:
                if j != father:
                    if not dfn[j]:
                        tarjan(j, i)
                        low[i] = min(low[i], low[j])
                        if dfn[i] < low[j]:
                            res.append([i, j])
                    elif j in v:
                        low[i] = min(low[i], low[j])
        tarjan(0, -1)
        return res