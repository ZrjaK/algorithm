# 题目：1203.项目管理
# 难度：HARD
# 最后提交：2022-10-14 20:21:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

from collections import defaultdict


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # 将不属于任何组的单独成组赋予组编号并记录每个组的成员
        d = defaultdict(list)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            d[group[i]].append(i)
        # 记录组间的拓扑关系与组内的拓扑关系
        outgroup_edge = defaultdict(list)
        ingroup_edge = defaultdict(lambda: defaultdict(list))
        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    ingroup_edge[group[i]][j].append(i)
                else:
                    outgroup_edge[group[j]].append(group[i])

        # 检查网络拓扑是否可行
        def check(edge, nodes):
            degree = defaultdict(int)
            for j in edge:
                for i in edge[j]:
                    degree[i] += 1
            ans = []
            stack = [i for i in nodes if not degree[i]]
            while stack:
                ans += stack
                nex = []
                for j in stack:
                    for i in edge[j]:
                        degree[i] -= 1
                        if not degree[i]:
                            nex.append(i)
                stack = nex[:]
            return ans if len(ans) == len(nodes) else []
        
        # 确定组间的可行顺序
        inter_order = check(outgroup_edge, list(set(group)))
        if not inter_order:
            return inter_order
        # 确定组内的可行的顺序        
        res = []
        for g in inter_order:
            inner_order = check(ingroup_edge[g], d[g])
            if not inner_order:
                return []
            res += inner_order
        return res