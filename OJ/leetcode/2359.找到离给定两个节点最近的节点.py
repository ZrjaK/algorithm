# 题目：2359.找到离给定两个节点最近的节点
# 难度：MEDIUM
# 最后提交：2022-07-31 10:52:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        route1 = [-1] * n
        route1[node1] = 0
        t = node1
        c = 0
        visited = set([node1])
        while edges[t] != -1:
            if edges[t] in visited:
                break
            c += 1
            route1[edges[t]] = c
            visited.add(edges[t])
            t = edges[t]
        route2 = [-1] * n
        route2[node2] = 0
        t = node2
        c = 0
        visited = set([node2])
        while edges[t] != -1:
            if edges[t] in visited:
                break
            c += 1
            route2[edges[t]] = c
            visited.add(edges[t])
            t = edges[t]
        # print(route1, route2)
        ans = -1
        t = 1e99
        for i in range(n):
            if route1[i] != -1 and route2[i] != -1:
                if max(route1[i], route2[i]) < t:
                    t = max(route1[i], route2[i])
                    ans = i
        return ans