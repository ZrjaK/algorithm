from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        d = defaultdict(set)
        for i, j in connections:
            d[i].add(j)
            d[j].add(i)
        dfn = [0] * n
        low = [0] * n
        index = 0
        bridge = []
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
        return bridge

# https://leetcode.cn/problems/critical-connections-in-a-network/submissions/

# 1192. 查找集群内的「关键连接」